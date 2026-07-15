# Specifications

!!! info "Official source — configuration dependent"

    These are selected values from the TRON 2 User Manual v0.1. They are not yet checked against the Ubbink unit. Do not use this table for design approval or safety limits.

| Category | Published value |
| --- | --- |
| Arm joints | 7 DoF per arm |
| Leg joints | 5 DoF per leg |
| Head | 2 DoF where fitted |
| Dual-arm shoulder width | 447 mm |
| Arm length without gripper | 730 mm |
| Biped overall width / standing height | 453 mm / 987 mm |
| Wheeled-biped overall width / standing height | 478 mm / 1015 mm |
| Top expansion area | 146 mm wide × 170 mm deep |
| Main battery | 46.8 V, 9 Ah |
| Single-arm published payload | 5 kg fully extended; 3 kg rated |
| Published repeatability | ±0.5 mm |
| Published teleoperation latency | 100 ms |

## Model-file specifications

Kinematic names, frames, axes, joint limits, collision meshes, and simulated sensors must be read from the exact `robot-description` variant and commit used by the project. Do not merge values across variants.

## Source

LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, section 1.2; [robot-description repository](https://github.com/limx-tron2/robot-description).
