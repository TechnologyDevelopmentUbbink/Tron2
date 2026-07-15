# Connections, ports, and indicators

!!! info "Official source — hardware match pending"

    Port labels below come from the TRON 2 User Manual v0.1. Verify them against the physical Ubbink robot before connecting equipment.

## Rear expansion panel

| Interface | Published description | Handling note |
| --- | --- | --- |
| 24 V input | Main power input | Use only the intended power source and connector |
| 12 V output | Stable DC accessory output; manual lists a 5 A maximum | Confirm accessory load and polarity before connection |
| USB 3.0 | Three ports shown in the manual | Check power and bandwidth requirements |
| Ethernet | Three Gigabit Ethernet ports shown | Network settings are configuration-specific |

## Body status light

| Pattern | Meaning in the manual |
| --- | --- |
| White, slow flash | Startup self-test |
| Red, steady | Fault detected |
| Red, flashing | Low main battery |
| Red, fast flashing | Critically low main battery |
| Yellow, flashing | Physical emergency stop is active |
| Blue, steady | Remote-control or VR teleoperation mode, depending on configuration |
| Sky blue, steady | High-level developer mode |
| Green, steady | Low-level developer mode |
| Purple, dynamic | Wheeled-biped stair mode |
| Yellow, breathing | Off-ground detection state |

!!! warning "Do not diagnose by color alone"

    Confirm the active mode on the controller/application and inspect diagnostic data. Similar colors can represent different states.

## Source

LimX Dynamics, *TRON 2 User Manual*, TRON 2 EDU edition, v0.1, 11 June 2026, sections 1.4 and 3.5.
