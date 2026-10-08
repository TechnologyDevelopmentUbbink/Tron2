# Operation

Start with [Safety](../getting-started/safety.md) and identify the [robot configuration and model](../hardware/robot-overview.md). Before movement, follow [Startup](startup.md) and confirm the robot state. Keep the [emergency-stop procedure](emergency-stop.md) within reach.

| Task | Page | Verification |
| --- | --- | --- |
| Prepare and power on | [Startup](startup.md) | Official-source summary; Ubbink verification pending |
| Handheld/VR control | [Controller & VR](../hardware/controller.md) | Official-source mappings; configuration dependent |
| Normal power down | [Shutdown](shutdown.md) | Official-source summary; Ubbink verification pending |
| Run and stop a learned policy | [Policy session](../deployment/run-a-policy.md) | Own-model session recorded 1 October; see scoped test evidence |
| Stop unsafe motion | [Emergency stop](emergency-stop.md) | Read before operation |

!!! warning "Check the active mode"

    The controller display and body light indicate modes such as idle, remote control, VR teleoperation, and developer operation. A button combination can have different prerequisites by configuration; never command motion until the mode and robot identity are confirmed.

## Minimum operator record

- Robot configuration/model
- Task and approved operating area
- Battery condition
- Controller/headset/application version where relevant
- Active mode and link status
- Stop path tested/accessible
- Observer or second person where required by the risk assessment
