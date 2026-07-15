# C++ low-level API

The official C++ API uses a `Tron2` singleton. The guide documents this core surface:

| API | Role |
| --- | --- |
| `Tron2::getInstance()` | Obtain the single robot API instance |
| `init(...)` | Initialize communication for the selected environment/interface |
| `getMotorNumber()` | Return the configured motor count |
| `subscribeImuData(...)` | Register an IMU callback |
| `subscribeRobotState(...)` | Register a robot-state callback |
| `publishRobotCmd(...)` | Publish motor command data |
| `subscribeSensorJoy(...)` | Register handheld-controller data callback |
| `subscribeDiagnosticValue(...)` | Register diagnostics callback |
| `setRobotLightEffect(...)` | Request a documented light effect |

!!! danger "Command publication"

    `publishRobotCmd` can produce physical motion. Validate the model, command vector length/order, limits, update rate, watchdog behavior, and stop path in simulation before hardware use.

## Minimal lifecycle (non-operational)

```cpp
// Structure only: fill parameters from the installed SDK documentation.
auto* robot = limxsdk::Tron2::getInstance();
// robot->init(...);
// register state/diagnostic callbacks
// verify target and state
// publish commands only under an approved test procedure
```

## Source

LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, section 2.1. Consult the matching SDK headers for authoritative signatures.
