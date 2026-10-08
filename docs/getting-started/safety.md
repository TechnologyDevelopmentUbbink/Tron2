# Safety

!!! danger "The robot can move or fall unexpectedly"

    Keep people outside the operating area, keep the physical emergency stop accessible, remove loose objects, and never stand in fall, crush, pinch, wheel, arm, or end-effector zones.

## Before operation

1. Read this Safety page and the current [official manual](https://limx.cn/en/documents/852949782845591552).
2. Make sure the operating area is clear of people, obstacles, and loose objects.
3. Check the [battery and charger](../hardware/battery-and-charger.md) and connectors for damage or abnormal condition.
4. Learn the [controller and emergency-stop controls](../hardware/controller.md) before enabling motion.
5. Make sure the external E-stop button is connected and within reach.

## Stop versus emergency stop

- Use the normal return and [shutdown](../operation/shutdown.md) sequence when conditions are controlled.
- Use an [emergency stop](../operation/emergency-stop.md) when continued powered motion is unsafe.
- Expect the robot to drop or become compliant when motor power is cut.
- Investigate the cause before reset or restart.

## Source

LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, “Safety and Responsibility Guidelines” and operation sections.
