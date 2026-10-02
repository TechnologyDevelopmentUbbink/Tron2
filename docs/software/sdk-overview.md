# SDK and software

The official SDK guide exposes two development layers.

| Layer | Purpose | Typical interfaces |
| --- | --- | --- |
| Low-level motion control | Develop and deploy motion-control algorithms in simulation or on hardware | C++/Python singleton, initialization, motor count, IMU/state subscriptions, command publication, controller and diagnostics callbacks, light effects |
| High-level application | Build applications on top of LimX-provided motion behavior | Dual-arm movement/state, emergency stop, light effects, grippers, robot management, and configuration-specific actions |

!!! warning "Developer mode can command real hardware"

    Confirm simulation versus hardware, the robot model, command limits, and stop path before initializing an SDK connection. Example code is not an operating procedure.

## Supported environments described by the SDK guide

- Linux x86-64
- Linux AArch64
- Windows (Python wheel in the public low-level SDK repository)
- ROS 1, ROS 2, and non-ROS use through the low-level API

## Start here

1. [Identify the robot and model assets](../hardware/robot-overview.md).
2. Choose [C++](../programming/cpp.md) or [Python](../programming/python.md) and follow the matching official package instructions.
3. Review the [high-level API map](../programming/api-reference.md).
4. Record exact firmware, SDK, ROS, and model versions in [Version compatibility](version-compatibility.md).

## Official public repositories

- [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)
- [TRON 2 robot-description](https://github.com/limx-tron2/robot-description)

## Source

LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, dated 13 January 2026 with cover identifier 20260225, sections 1–3.
