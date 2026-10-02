# Measure task success on the robot

A running inference chain is not a successful pick-and-place policy. Record repeated trials using a defined task and starting arrangement.

## Trial protocol

1. Use a fixed set of ring positions, for example five positions repeated twice per model.
2. Alternate models/settings so light, temperature and wear affect both.
3. Count success only when the ring finishes in the red bin without intervention.
4. Record the failure mode: missed grasp, drop, collision, freeze or emergency stop.
5. Keep an operator at the emergency stop throughout.

The local trial format uses `model,poging,geslaagd,opmerking`: model, attempt, success 0/1 and remark. Treat different playback settings as different conditions, for example ACT with ten actions per refresh versus a full chunk.

## Report uncertainty

The local `proeven` utility reports success rate with a 95% Wilson interval. Its non-overlapping-interval rule is a conservative comparison heuristic; overlapping intervals do not by themselves prove equal performance. A suggested trial count is approximate.

Ten attempts per condition can distinguish only large differences. Keep trial counts and failure modes beside percentages.

## Current evidence

The 1 October session demonstrated execution and fault handling. It did not establish a repeated task-success rate or generalisation. [Session record](../projects/experiments/2026-10-01-robot-session.md).

**Source:** [UBB-IL-001](../reference/document-sources.md), section 7.4; [UBB-POL-001](../reference/document-sources.md), section 17.7.
