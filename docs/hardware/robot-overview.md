# Robot overview

The TRON 2 is described by LimX as a modular research platform. The official material separates an EDU edition from a standard edition and shows multiple physical configurations. Never assume a procedure or specification applies to every configuration.

## Configuration families

<div class="configuration-families" markdown>

| Family | What the source describes | Main wiki topics |
| --- | --- | --- |
| **Dual-arm — Ubbink robot (`DACH_TRON2A`)** | Two seven-axis arms; optional grippers or dexterous hands; VR teleoperation in the EDU material | [Controller & VR](controller.md), [SDK](../software/index.md) |
| Bipedal | Two five-axis legs and handheld remote operation | [Controller](controller.md), [Operation](../operation/index.md) |
| Wheeled-biped | Leg configuration with wheels and a dedicated stair/flat-ground mode | [Controller](controller.md), [Operation](../operation/index.md) |
| Mobile dual-arm | Dual-arm platform combined with a mobile chassis and lift | VR/mobile-chassis controls are configuration-specific |

</div>

## Public robot-description models

The official public repository currently organizes assets by variant folder:

`DA_TRON2A`, `DACH_TRON2A`, `WF_TRON2A`, `SF_TRON2A`, `WFYG_TRON2A`, and `SFYG_TRON2A`.

Each variant can contain `urdf/`, `xacro/`, `xml/`, `meshes/`, and, for some variants, `usd/`. The repository documents a floating base, ROS-style axes unless an integration states otherwise, and variant-dependent sensor geometry.

## Sources

- LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, section 1.
- [LimX TRON 2 robot-description repository](https://github.com/limx-tron2/robot-description), accessed for repository layout and variant names.
