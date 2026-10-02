# The client and its watchdogs

**Measured behaviour:** losing the client's servoj stream makes the arms enter emergency stop and drop. If only the policy server fails, a live client can keep sending the last target and hold position.

That is why watchdogs belong in the client. A failed server cannot perform its own recovery.

## Fault handling

| Condition | Response in the tested client |
| --- | --- |
| No fresh server answer | Warn after 1 s; start rest handling after 10 s |
| Bridge/observation stall | Controlled rest handling after the 5 s observation budget |
| Connect + warm-up | Separate 30 s budget |
| Conversion error, normal end, Ctrl+C or SIGTERM | Rest route before shutdown |
| Wrong state/action dimension | Refuse incompatible execution |
| Policy start pose not reached | Return to rest; do not query the policy |
| Rest route fails | Keep the stream alive and hold; manual intervention required |

The original observation timeout raised an exception that killed the producer thread. The revised client catches that fault and preserves the stream during recovery. Thread joins must not quietly add several seconds to the watchdog threshold.

## Check movement, not a success message

A log saying “init pose reached” can appear even when the robot did not move. Read state feedback. The client reports **ROBOT BEWOOG NIET** when a commanded move changes the pose by less than 0.01 rad. An identical large arrival error on repeated attempts can mean no motion occurred.

## What the tests prove

Fault tests used a mock robot, Bridge and network with the real SmolVLA server. The mock judged whether the command stream dropped, rather than trusting the client's own success report. Running the original client as a negative control caused the simulated arms to drop after one second.

These checks support the handled fault paths. They do not eliminate hard-crash, power-loss or robot-link failure risk. See the [test matrix](../projects/experiments/2026-09-30-deployment.md) and [real fault](../projects/experiments/2026-10-01-robot-session.md).

## Motor release remains manual

The tested runtime exposed no normal motor-release command. The operator's handheld action bypasses the client connection. The order is controlled return to rest, then manual release; emergency stop is a different mechanism.

**Source:** [UBB-CLIENT-001](../reference/document-sources.md), sections 16.1–16.3 and 16.7; [UBB-POL-001](../reference/document-sources.md), section 17.5.
