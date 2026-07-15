# Robot overview

<div class="wiki-facts" markdown>

| | |
| --- | --- |
| **Platform** | Modular embodied-robotics research platform |
| **Documented edition** | TRON 2 EDU |
| **Configurations in the manual** | Dual-arm, bipedal, wheeled-biped |
| **Development languages** | C++ and Python |
| **Model assets** | URDF, Xacro, MuJoCo XML, meshes; USD for some variants |
| **Verification** | Official source; Ubbink hardware match pending |

</div>

The TRON 2 is described by LimX as a modular research platform. The official material separates an EDU edition from a standard edition and shows multiple physical configurations. Never assume a procedure or specification applies to every configuration.

!!! info "Version dependent"

    Identify the installed modules and the robot-model identifier before selecting software, model files, limits, or controller mappings.

## Configuration families

| Family | What the source describes | Main wiki topics |
| --- | --- | --- |
| Dual-arm | Two seven-axis arms; optional grippers or dexterous hands; VR teleoperation in the EDU material | [Controller & VR](controller.md), [SDK](../software/index.md) |
| Bipedal | Two five-axis legs and handheld remote operation | [Controller](controller.md), [Operation](../operation/index.md) |
| Wheeled-biped | Leg configuration with wheels and a dedicated stair/flat-ground mode | [Controller](controller.md), [Operation](../operation/index.md) |
| Mobile dual-arm | Dual-arm platform combined with a mobile chassis and lift | VR/mobile-chassis controls are configuration-specific |

## Public robot-description models

The official public repository currently organizes assets by variant folder:

`DA_TRON2A`, `DACH_TRON2A`, `WF_TRON2A`, `SF_TRON2A`, `WFYG_TRON2A`, and `SFYG_TRON2A`.

Each variant can contain `urdf/`, `xacro/`, `xml/`, `meshes/`, and, for some variants, `usd/`. The repository documents a floating base, ROS-style axes unless an integration states otherwise, and variant-dependent sensor geometry.

## Identify the Ubbink robot

Record these items before adding verified procedures:

| Item | Ubbink value |
| --- | --- |
| Robot model identifier | Not recorded |
| Serial-number evidence location | Not recorded; do not publish the serial number |
| Installed configuration/modules | Not recorded |
| Hardware revision | Not recorded |
| Firmware/software versions | Not recorded |

## Sources

- LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, section 1.
- [LimX TRON 2 robot-description repository](https://github.com/limx-tron2/robot-description), accessed for repository layout and variant names.
