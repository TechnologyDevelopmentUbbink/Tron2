# Robot models & Isaac Lab

The following setup notes are a dated public-documentation snapshot; they are distinct from our own LeRobot environment. Verify upstream requirements before a new installation.

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


## Sources

[Original stack overview](../software/isaac-sim-training.md#sources).
