# Red ring pick-and-place

The shared proof-of-concept is to pick up the red ring and place it in the red bin.

| Route | Approach |
| --- | --- |
| Simulation | Train with Isaac Sim/Isaac Lab; physical transfer depends on robot, gripper and workplace fidelity |
| Physical imitation | Record VR demonstrations; train ACT or SmolVLA with LeRobot |
| LimX policy tests | Exercise the deployment chain; published tasks have their own cell/object requirements |

## What has been established

The physical recording, cleaning, training, evaluation and deployment chain works. SmolVLA ran on the real robot on 1 October, with zero reported stalls in 926 steps. Client fault handling was also exercised on a real camera-startup failure.

## What those results do not establish

Four training episodes were insufficient for held-out generalisation. ACT and SmolVLA both performed worse than the hold baseline in the first real-data test, despite strong training-episode performance. No repeated robot task-success rate is supplied.

In simulation, earlier reward experiments exposed a lift term paying for a tap, a goal term paying in the start state, and a holding term satisfied by jaws touching the ring from outside. Those are lessons about checking what a metric rewards, not complete simulation-training instructions.

## Evidence and next measurement

[Real-data comparison](experiments/2026-09-29-real-data.md) · [Robot session](experiments/2026-10-01-robot-session.md) · [Trial protocol](../learning/robot-trials.md).

More demonstrations and controlled repeated trials are the next evidence needed for task quality. Keep the deployment-chain and task-quality verdicts separate.

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 1, 7.3 and 10a–10b; [UBB-POL-001](../reference/document-sources.md), section 17.7.
