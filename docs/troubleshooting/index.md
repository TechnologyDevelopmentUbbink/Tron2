# Troubleshooting

Start with observation and evidence. Do not repeatedly power-cycle or re-enable motors when the cause is unknown.

## First triage

1. Stop motion and make the area safe.
2. Record the robot configuration and active mode.
3. Photograph or transcribe body-light pattern and controller display without exposing secrets or serial numbers.
4. Record battery level, controller link, error code, firmware/SDK/app versions, and the last successful action.
5. Decide whether the fault is power, control mode, network, software, or mechanical.

| Symptom | Initial checks |
| --- | --- |
| Slow white body flash persists | Startup/self-test not complete; wait, then collect diagnostics instead of commanding motion |
| Steady red body light | Fault detected; record controller/diagnostic error and stop normal operation |
| Flashing red | Low or critical battery indication; follow battery procedure |
| Flashing yellow | Physical emergency stop active |
| Controller has no signal bars | Target robot, controller power, distance/interference, pairing/link state |
| SDK cannot initialize | Target/model, network interface, architecture/package version, service state |
| Command rejected | Mode/prerequisite, units/ranges, request format, illegal-command response |

## Escalation record

```text
Robot configuration/model:
Firmware/SDK/application versions:
Time and operating mode:
Last known good state:
Exact action before fault:
Indicators/error code:
Reproducible (yes/no):
Evidence location:
```

!!! warning "Sensitive data"

    Remove credentials, fixed network addresses, serial numbers, personal data, and internal Ubbink information before attaching logs or screenshots to a public issue.
