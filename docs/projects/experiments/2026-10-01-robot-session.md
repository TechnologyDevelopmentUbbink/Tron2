# 1 October — real robot session

The own SmolVLA policy ran through the shared client on the real robot.

| Measurement | Reported result |
| --- | --- |
| Inferences | 92 |
| End-to-end inference | 108 ms |
| Execution/prediction horizon | s=10/H=50 |
| Executed steps | 926 |
| Stalls | 0 |
| Final route arrival errors | 0.078 / 0.032 / 0.065 rad |
| Action clipping | 37–44 of 900 values |
| Intervention in the completed run | None reported |

This demonstrates execution, timing and the return path. It does not supply a repeated task-success rate.

## Camera startup failure

The session report also records `first_frame_timeout` on all three cameras. The client caught the fault and attempted the rest route. Arrival failed, so it held the arms instead of exiting.

This is physical evidence for the failed-rest handling branch. It does not identify why the cameras failed, and it must not be merged into the zero-stall successful run as if they were one uninterrupted result.

## Still to distinguish

The source says the underlying own-model shortcut path was built/tested while the actual desktop click was unverified. On 2 October the owner reported the LimX shortcut newly built but untested. Firmware and zeroing remained unchanged.

**Source:** [UBB-POL-001](../../reference/document-sources.md), section 17.7; owner clarifications 2 October.
