# Simulation & physical teleoperation

Keep the physical PICO recording workflow separate from CloudXR simulation teleoperation. Hardware in common does not establish that the software is the same.

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


## Recordings for imitation learning

Our measured workflow uses real TRON 2 recordings in LeRobot format. Follow [Demonstrations](../learning/demonstrations.md) and [Dataset quality](../learning/dataset-quality.md), regardless of how the recorder is implemented.

## Sources

[Original stack overview](../software/isaac-sim-training.md#sources). Upstream headset, workstation and framework support must be checked for the version being installed.
