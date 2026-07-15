# Controller and VR headset

This page maps the official handheld and VR controls for the configurations covered by the TRON 2 User Manual.

!!! danger "Read before operating"

    These mappings are **official-source summaries, not Ubbink-verified instructions**. Confirm the robot configuration, clear the operating area, keep the physical emergency stop accessible, and start at low risk. Several emergency commands cause the robot to drop.

## Handheld controller

The controller has a D-pad, two joysticks with push buttons, face buttons (`△`, `○`, `×`, `□`), shoulder buttons (`L1`, `L2`, `R1`, `R2`), a display, and a power button. The display reports radio signal, controller battery, robot state information, and current mode.

### Common and dual-arm commands

| Purpose | Input | Required state | Important behavior |
| --- | --- | --- | --- |
| Change mode | `R1` + right face button | Idle | Dual-arm cycles VR teleoperation / developer mode; leg configurations cycle remote-control / developer mode |
| Return action | `L1` + `×` | Remote-control or high-level developer mode | Dual-arm lowers/returns arms; leg configurations squat/fold; then enters idle |
| Enter idle immediately | `L1` + `□` | Global | Skips return action; joints enter damping and the robot can drop. Emergency use only |
| Emergency stop | Push both joystick buttons | Global | Motor drives are cut immediately; the robot can drop |
| Release controller e-stop | Push right joystick button | E-stop state | Motors are re-enabled and the robot enters damping state |
| Zero calibration | `L1` + `R1` | Idle | Only after controller upgrade or confirmed zero-position loss/drift; follow the full manual procedure |

### Bipedal and wheeled-biped commands

| Purpose | Input | Required state |
| --- | --- | --- |
| Enter ready state | `L1` + `○` | Idle or standing |
| Stand in place | `L1` + `△` | Ready |
| Move forward/back | Left joystick up/down | Standing |
| Move left/right | Left joystick left/right | Standing; biped only |
| Turn in place | Right joystick left/right | Standing |
| Adjust body height | Hold `R1` + D-pad up/down | Standing |
| Switch flat/stair mode | Hold `□` for 2 s | Standing; wheeled-biped only |
| Fall recovery | `L2` + `△` | Fall detected |

!!! warning "Configuration-specific controls"

    Do not use a biped/wheeled-biped command table on a dual-arm configuration, or vice versa. The same combination can have a different prerequisite or outcome.

## VR teleoperation

The manual identifies the supported EDU teleoperation device as a PICO 4 Ultra. The two VR controllers provide joysticks, grip buttons, triggers, face buttons, and home/menu controls.

### Dual-arm VR controls

| Purpose | Input | Required state |
| --- | --- | --- |
| Start teleoperation / establish initial zero | Hold both grip buttons for more than 1 s | Robot in VR teleoperation mode |
| Return arms to initial zero | Hold both grip buttons for more than 1 s | Active teleoperation |
| Move end effectors | Move the held VR controllers | Initial-zero or active teleoperation state |
| Pause/resume left arm | Left-controller `X` | Initial-zero or active teleoperation state |
| Pause/resume right arm | Right-controller `A` | Initial-zero or active teleoperation state |
| Toggle left gripper | Left trigger | Initial-zero or active teleoperation state |
| Toggle right gripper | Right trigger | Initial-zero or active teleoperation state |
| Start data collection | Right-controller `B` | Active teleoperation |
| Stop data collection | Right-controller `B` again | Collection active |

### Mobile chassis and lift (where fitted)

| Purpose | Input |
| --- | --- |
| Forward/backward | Left joystick forward/back |
| Ackermann steering | Right joystick left/right in Ackermann mode |
| Select diagonal mode | Hold right joystick for 1 s |
| Select Ackermann mode | Hold left joystick for 1 s |
| Parking state | Hold left-controller grip and right-controller joystick for 1 s |
| VR emergency stop | Push both VR joysticks |
| Raise/lower lift | Hold right grip and move left joystick forward/back |

## Preparing a VR session

1. Confirm the exact robot configuration and the supported headset/application version.
2. Complete robot startup and confirm the area is clear.
3. Put the robot into VR teleoperation mode using the handheld controller.
4. Connect the headset using the approved robot network profile. Credentials and fixed addresses are intentionally not published here.
5. Start the official teleoperation application and verify its target robot before granting control.
6. Establish the initial-zero state, verify both arms at low risk, then begin work.

!!! note "Calibration is exceptional"

    The manual says zero calibration is required only after a controller upgrade or severe impact causing zero-position loss or drift. It is not a normal startup step.

## Ubbink verification record

| Item | Value |
| --- | --- |
| Robot configuration tested | Not tested |
| Robot firmware | Not recorded |
| Handheld controller version | Not recorded |
| VR headset/app version | Not recorded |
| Verified by | Not reviewed |

## Source

LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, sections 4 and 5. Tables are paraphrased; consult the source for complete prerequisites, warnings, and illustrations.
