# Isaac Sim, Isaac Lab & FluxVLA Training

Source status: internet-sourced, unofficial (LimX + NVIDIA public repos/docs). Not yet Ubbink-verified against the official manual.

This page covers the simulation, training, and teleoperation stack around the TRON 2 EDU (dual-arm), separate from the onboard SDK covered in [Installation](../software/installation.md).

## Software layers

LimX's stack is organized in three layers:

- **System 0** — whole-body motion foundation model
- **System 1** — VLA/WAM skills + AI infrastructure (this is where FluxVLA lives)
- **System 2** — COSA, an agent OS for LLM/world-model-based reasoning and planning

**FluxVLA Engine** is the open-source training framework for System 1: data handling, simulation training, real-robot iteration, and deployment. Supports OpenVLA, LlavaVLA, GR00T, Pi0, and Pi0.5 on Llama/Gemma/Qwen backbones.

!!! warning "Isaac Sim support status"
    Native Isaac Sim support is listed as an open TODO item in the FluxVLA repository itself. Training data currently comes mainly from LIBERO (MuJoCo-based) and real-robot demonstrations. Isaac Sim/Isaac Lab is a separate, parallel path — not a built-in part of FluxVLA.

- Repo: [`limxdynamics/FluxVLA`](https://github.com/limxdynamics/FluxVLA)
- Docs: `fluxvla.limxdynamics.com`

## Robot model (URDF/USD) for Isaac Sim

Official model files: [`limxdynamics/robot-description`](https://github.com/limxdynamics/robot-description)

Contains URDF/xacro, MuJoCo XML, meshes, and optional USD assets — usable directly in Isaac Sim. If no ready-made `.usd` is present for a variant, import the URDF via Isaac Sim's built-in URDF Importer extension.

**Steps:**

1. `git clone https://github.com/limxdynamics/robot-description.git`
2. Select the TRON 2 variant matching your configuration (dual-arm/desktop)
3. If no `.usd` present: Isaac Sim → Extensions → URDF Importer → point to the `.urdf`
4. Verify the Articulation Root and collision meshes after import — the most common source of silent physics failures

## Isaac Lab RL training

Separate Isaac Lab training stacks exist in the LimX GitHub org for SF/WF and SFYG/WFYG variants, and specifically for the 6-DoF arm + gripper variants (locomotion policy training + play mode). Search `github.com/limxdynamics` for `isaaclab` + `tron2` — repo names change frequently.

### Running on a DGX Spark

RL training runs fine on a DGX Spark (aarch64), provided you follow the source-build install route:

- Build from source (aarch64) rather than the standard x86 pip install
- GCC/G++ 11 as default compiler, CUDA ≥ 13.0, Git LFS
- NVIDIA driver 580.95.05 recommended
- Setup takes ~15–20 minutes, needs ~50GB free disk
- Cosmos Transfer1 is not yet supported on DGX Spark
- SkillGen (Isaac Lab Mimic extension) is limited on DGX Spark due to cuRobo CUDA/C++ extensions

!!! danger "XR teleoperation is not supported on DGX Spark"
    Confirmed in current Isaac Lab documentation: *"Extended reality teleoperation tools such as OpenXR is not supported [on DGX Spark]. This is due to encoding performance limitations."* This is a hardware encoding limitation, not a temporary software gap. CloudXR-based simulation teleoperation (below) requires a separate workstation.

## Simulation teleoperation via CloudXR

For recording demonstrations **inside the simulation** (not on the physical robot), Isaac Lab supports XR teleoperation via NVIDIA CloudXR. Apple Vision Pro is the reference implementation; Meta Quest 3 / Pico 4 Ultra are supported via the CloudXR Early Access program.

**Workstation requirements** (separate from the DGX Spark, per the limitation above):

- Ubuntu 22.04/24.04
- 16-core CPU (e.g. Threadripper Pro 5955WX class)
- 64GB RAM
- 1x RTX PRO 6000 or RTX 5090-class GPU
- Docker 26+, Docker Compose 2.25+, NVIDIA Container Toolkit
- Dedicated Wifi 6 router recommended

**Retargeting notes:**

- `Se3RelRetargeter` — relative/incremental control, good for precision work
- `Se3AbsRetargeter` — 1:1 absolute end-effector mapping
- `GripperRetargeter` — gripper open/close from thumb-index distance
- No ready-made retargeter exists for the TRON2/BrainCo hand geometry — write or adapt one
- Dexpilot optimizer needs five fingertip points + palm; fingertip links must sit exactly on the fingertip geometry or IK optimization fails silently

**Performance tuning:** match `sim.dt` to headset refresh (`1/90` for AVP with `render_interval=2` ≈ 45Hz effective), run physics on CPU for single-environment teleop, set `NV_PACER_FIXED_TIME_STEP_MS` on the CloudXR runtime container for consistent pacing.

Reference: [Isaac Lab CloudXR teleoperation guide](https://isaac-sim.github.io/IsaacLab/main/source/how-to/cloudxr_teleoperation.html)

## Local teleoperation on the physical robot (Pico 4 Ultra)

Separate from the simulation route above: the TRON 2 EDU supports teleoperation directly on the physical robot via the onboard i7 computebox and the bundled Pico 4 Ultra Enterprise headset.

Since mid-2026, NVIDIA and PICO have jointly released **Isaac Teleop**, an open-source framework that intentionally does not separate sim and real-robot teleoperation — same device workflow, same data schema, for both Isaac Sim/Isaac Lab and a physical robot via Isaac ROS. Pico 4 Ultra (Enterprise) is the primary supported headset (needed for VST passthrough / egocentric capture).

**Data layer:** FlatBuffers schema, `.mcap` recording, explicit LeRobot-format interoperability — the same format FluxVLA uses for training.

!!! question "Open question"
    Not confirmed whether LimX's own teleop app on the i7 computebox is built on top of this NVIDIA/PICO Isaac Teleop framework, or is a separate closed implementation that happens to also use Pico hardware. Check on the robot itself for an `isaacteleop` or `isaac_ros_teleop` package, or ask LimX support (`contactus@limxdynamics.com`).

- Repo: [`NVIDIA/IsaacTeleop`](https://github.com/NVIDIA/IsaacTeleop)
- ROS2 package: [`NVIDIA-ISAAC-ROS/isaac_ros_teleop`](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_teleop)
- Docs: [Isaac Teleop quick start](https://nvidia.github.io/IsaacTeleop/main/getting_started/quick_start.html)

## Deploying a trained model on the robot

Two different paths depending on model type:

**RL policy (locomotion/motion control):** small model, exported as ONNX, runs directly on the i7 computebox — no external GPU needed.

**VLA policy (manipulation, pi0/pi0.5/GR00T from FluxVLA):** too heavy for the i7. Standard pattern (OpenPI architecture, which FluxVLA builds on): a policy server on a separate GPU machine loads the checkpoint; the robot runs only a lightweight client that sends camera + joint data over WebSocket and executes the returned action — repeated in a control loop.

A DGX Spark is well suited to running the policy server itself (128GB unified memory, up to 1 petaFLOP FP4) — this is explicitly the kind of local large-model inference workload it's designed for, unlike the XR rendering path above.

```
# Server (on DGX Spark)
uv run scripts/serve_policy.py policy:checkpoint \
  --policy.config=<config> --policy.dir=<checkpoint_dir> --port=8000

# Client (on TRON2 i7 computebox)
websocket_client_policy.WebsocketClientPolicy(host="<dgx-spark-ip>", port=8000)
```

LimX maintains a TRON2-specific derivative of OpenPI (policy transforms, deployment config templates, pi0/pi0.5 serving, real-robot client examples) plus a separate TRON2 runtime package handling WebSocket robot communication, motion execution, and observation collection.

## Sources

| Source | URL |
|---|---|
| Robot model (URDF/USD/MuJoCo) | `github.com/limxdynamics/robot-description` |
| FluxVLA Engine | `github.com/limxdynamics/FluxVLA` |
| FluxVLA docs | `fluxvla.limxdynamics.com` |
| All LimX repos | `github.com/limxdynamics` |
| Isaac Lab docs | `isaac-sim.github.io/IsaacLab` |
| Isaac Lab CloudXR guide | `isaac-sim.github.io/IsaacLab/main/source/how-to/cloudxr_teleoperation.html` |
| Isaac Teleop (NVIDIA/PICO) | `github.com/NVIDIA/IsaacTeleop` |
| Isaac ROS Teleop | `github.com/NVIDIA-ISAAC-ROS/isaac_ros_teleop` |
| OpenPI | `github.com/Physical-Intelligence/openpi` |
| DGX Spark + Isaac install guide | `learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/` |

*Repo names and framework details change frequently (active development, mid-2026). Verify against current docs before cloning/installing.*
