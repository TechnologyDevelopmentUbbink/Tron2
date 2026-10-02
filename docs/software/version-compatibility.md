# Version compatibility

The LeRobot environment and own-model serving chain were measured on GB10 in September/October. The complete installed robot firmware/SDK/ROS inventory remains incomplete; do not treat the tested learning environment as a verified inventory of the whole robot.

## Source snapshot

| Component | Value stated by supplied source | Status |
| --- | --- | --- |
| SDK guide | v0.5; revision 13 January 2026; cover 20260225 | Source imported |
| Developer OS | Ubuntu 20.04.6 LTS | Source snapshot only |
| ROS 2 | Foxy | Source snapshot only |
| ROS 1 | Noetic | Source snapshot only |
| User Manual | TRON 2 EDU v0.1; 11 June 2026 | Source imported |
| `robot-description` | Public `main` branch | Commit not pinned |

!!! info "A documented default is not a requirement"

    The actual robot image may differ from the SDK guide snapshot. Record installed values from the Ubbink unit before changing or installing software.

## Ubbink compatibility matrix

| Robot model/hardware | Firmware set | SDK commit/package | ROS | Model commit | Result |
| --- | --- | --- | --- | --- | --- |
| Not recorded | Not recorded | Not recorded | Not recorded | Not recorded | Not tested |

## Sources

LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, sections 1.3 and 6; [robot-description repository](https://github.com/limx-tron2/robot-description).



## Measured learning/serving combination

| Context | Recorded combination | Evidence |
| --- | --- | --- |
| GX10 / DGX Spark learning | Ubuntu 24.04, Python 3.12.3, driver 580.173.02, LeRobot 0.6.1, torch 2.11.0+cu130, TorchCodec 0.11.1+cu130 | Decoder/GPU checks; same evaluation reproduced on Spark |
| Own-model serving | Shared client + real SmolVLA server; three cameras, 18 state values | Mock faults and 1 October execution |
| LimX shortcut | Newly built | Untested as of 2 October |
| Robot calibration | No firmware/re-zero change since measurements | Owner confirmation 2 October |

[Full environment table](../learning/lerobot-setup.md) · [Experiments](../projects/experiments/index.md) · [Calibration implications](firmware.md).
