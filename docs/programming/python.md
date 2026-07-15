# Python low-level API

The Python binding mirrors the C++ concepts.

| Method | Role |
| --- | --- |
| Constructor / instance creation | Create the Python-side SDK object |
| `init(...)` | Initialize communication |
| `getMotorNumber()` | Get configured motor count |
| `subscribeImuData(...)` | IMU callback |
| `subscribeRobotState(...)` | Robot-state callback |
| `publishRobotCmd(...)` | Send motor command data |
| `subscribeSensorJoy(...)` | Handheld-controller callback |
| `subscribeDiagnosticValue(...)` | Diagnostic callback |
| `setRobotLightEffect(...)` | Light-effect request |

## Installation source

The official guide points to platform-specific wheels in the public [`limxsdk-lowlevel`](https://github.com/limxdynamics/limxsdk-lowlevel) repository. Select the wheel for the interpreter and CPU architecture; do not copy an old wheel filename from the wiki.

```bash
git clone https://github.com/limxdynamics/limxsdk-lowlevel.git
# Install the wheel matching this computer's platform and Python environment.
```

## Source

LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, section 2.2. Consult the installed package for authoritative signatures and message fields.
