# Shutdown

## Normal sequence

1. Stop commanded motion and clear nearby people.
2. Use the configuration-appropriate return action (`L1` + `×` in the cited manual) and allow the robot to settle in its return/idle posture.
3. Confirm the robot is stable before removing motor or battery power.
4. Power off the robot using the official power-button sequence.
5. Power off the handheld controller.
6. Wait until indicators are off before removing the battery.

!!! danger "Do not substitute emergency idle for normal shutdown"

    `L1` + `□` skips the controlled return action and can let the robot drop. It is documented as an emergency-only action when return fails.

## Source

LimX Dynamics, *TRON 2 User Manual*, v0.1, section 3.4.
