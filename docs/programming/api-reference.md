# High-level API map

The high-level application interface uses a structured request/response protocol. The guide documents these groups; exact fields and allowed ranges must be taken from the matching SDK release.

| Group | Documented operations |
| --- | --- |
| Dual-arm motion | `MoveJ`, `MoveP`, `ServoJ` |
| State queries | Joint state and end-pose retrieval |
| Safety/management | Emergency stop, light effects, basic information, illegal-command notification |
| LimX two-finger gripper | Set command and query state |
| Configuration-specific actions | Biped/wheeled-leg state and actions in the current online guide |

## Protocol workflow

1. Confirm communication format and request identifier rules.
2. Read the robot’s basic information/model.
3. Validate units, frames, joint order, limits, and response semantics.
4. Handle negative/illegal-command responses.
5. Subscribe to state feedback before commanding motion.
6. Test in simulation and under an approved hardware procedure.

!!! info "Online guide may be newer"

    The public online SDK guide contains sections beyond the supplied v0.5 PDF. Record which source revision was used for every implementation.

## Sources

- [TRON 2 SDK Development Guide (online)](https://limx.cn/en/documents/856848486581276672)
- LimX Dynamics, *TRON 2 SDK Development Guide*, v0.5, sections 3–4.
