# Emergency stop

!!! danger "The robot can drop"

    Both the physical and controller emergency-stop paths cut motor-drive power. Support/clear the robot as far as safely possible and keep people out of the fall and pinch zones.

## Emergency-stop triggers

| Method | Trigger | Indication/behavior |
| --- | --- | --- |
| External Emergency-stop button | Push the button | Motor power cut; body light flashes yellow |
| Physical robot e-stop | Operate the body emergency-stop control | Motor power cut; body light flashes yellow |
| Handheld controller | Push both joystick buttons | Motor power cut immediately; battery and indicators remain powered |
| VR controllers | Push both VR joysticks | Stops the robot/mobile chassis in VR operation |

## After an e-stop

1. Do not immediately re-enable motion.
2. Make the area safe and identify why the stop was needed.
3. Inspect the robot and load for damage, displacement, or trapped energy.
4. Release the physical e-stop only when authorized.
5. The cited handheld release command is the right joystick button; the robot enters damping state. Be ready for unpowered/compliant motion.
6. **Perform a full robot power cycle**: shut the robot down completely, then follow [Startup](startup.md). Releasing the E-stop alone does not clear the Ubbink robot’s error state; the body light remains red until a full power cycle.
7. Re-run startup checks and confirm the red error indication is cleared before resuming work.

The red-light error state and full power-cycle requirement are Ubbink hardware observations supplied in this documentation review.

## Source

LimX Dynamics, *TRON 2 User Manual*, v0.1, sections 3.5, 4.4, 4.5, and 5.2.
