# Startup

!!! danger "Configuration and environment check required"

    Use the current official manual and an approved operating area. The illustrations and starting posture differ between configurations.

## Before power-on

1. Identify whether the robot is dual-arm, bipedal, wheeled-biped, or mobile dual-arm.
2. Clear the operating area and keep people outside the safety distance stated in the current manual.
3. Inspect the robot, battery, connectors, modules, and physical emergency stop.
4. Use a fully charged, correct battery.
5. Place/support the robot in the configuration-specific starting posture shown by the official manual.

## Power-on sequence

1. Install the battery fully and confirm the latch is locked.
2. Use the robot power-button sequence shown in the current official manual.
3. Power on the handheld controller.
4. Observe the body indicator: a slow white flash means self-test is running.
5. Wait for the status light to become steady blue or green and confirm the handheld display shows a radio link.
6. Check the controller display for robot mode, power state, battery, and any error code before issuing motion commands.

!!! note "Why the exact button timing is not duplicated here"

    Startup timing is safety-critical and version dependent. The wiki intentionally points operators to the current official manual until Ubbink has verified the shipped hardware and recorded the procedure.

## Verification

- No red fault indication
- Controller link visible
- Expected control mode shown
- Battery level suitable for the task
- No unexpected sound, motion, heat, or message

## Source

LimX Dynamics, *TRON 2 User Manual*, v0.1, section 3.4.
