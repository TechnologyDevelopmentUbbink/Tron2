# Joint and command layouts

A matching vector length does not guarantee matching joint order. Grippers are interleaved with the arms in our state; they are not the last two elements.

## Measured TRON 2 / LeRobot / OpenPI state order

| Index | Channel | Unit |
| --- | --- | --- |
| 0–6 | Left arm, seven joints | rad |
| 7 | Left gripper | Opening fraction, 0–1 |
| 8–14 | Right arm, seven joints | rad |
| 15 | Right gripper | Opening fraction, 0–1 |
| 16 | Head pitch | rad |
| 17 | Head yaw | rad |

The joint-state query returns a dict containing timestamps, update flags and `states`. Only `states` is the flat vector; do not use `dict.values()` as positions.

## Command layouts are different

| Interface | Values | Order |
| --- | --- | --- |
| Joint state / own-model actions | 18 | L7, L-grip, R7, R-grip, head2 |
| 16-dimensional policy | 16 | L7, L-grip, R7, R-grip; head omitted |
| `command_joints` / servoj | 16 | L7, R7, head2; grippers commanded separately |
| `movej` | 14 | L7, R7; head uses its separate interface |
| FluxVLA record described in the proposal | 18 | L7, R7, head2, L-grip, R-grip |

The inspected runtime truncates the state to the configured dimension. Its action conversion removes the two grippers from the servoj vector. A 16-dimensional policy keeps the current head target; an 18-dimensional one includes a predicted head target.

Never confuse a 16-dimensional policy observation with the 16-value servoj command. Always validate the family, order and metadata.

## Grippers

The command converts a 0–1 opening fraction into percent for the separate gripper API. Fully open measured 80 mm on our robot. The recordings and deployed own-model cap use 0.94; that is a command limit, not proof of the SDK's internal clamp.

The recorded gripper “state” is command feedback, not measured jaw position. [Recording semantics](../learning/demonstrations.md#state-is-not-always-a-measurement).

**Source:** [UBB-IL-001](document-sources.md), sections 4.2, 8.7, 14.3 and 15.3; deployment-proposal appendix; August Bridge issue.
