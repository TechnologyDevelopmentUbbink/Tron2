# Evaluate behaviour, not training loss

Offline evaluation is a pre-selection on held-out recordings. The model sees recorded images and state; it does not experience the consequences of its own mistakes. Only robot trials establish task success.

## What the evaluator measures

Predictions are sampled every 0.25 seconds and compared over the next second.

| Measure | Meaning |
| --- | --- |
| Gripper timing | Switch hit rate within ±0.3 s, plus false-alarm rate |
| Short-lead timing | Hit rate for switches at most 0.3 s ahead |
| Grasp position | Mean absolute joint error in degrees for the relevant arm when the demonstration closes the gripper |
| Motion skill | `1 - model_error / hold_error` for arm groups that actually move |
| Arm error | Mean joint error over the prediction horizon, in degrees |

Skill errors are normalised per joint using recorded statistics. The head does not count in the arm score. Gripper classification uses hysteresis. The local rank combines timing hit rate and false alarms, then grasp-position error, then motion.

## Checks on the evaluator itself

An oracle using recorded actions must score perfectly. Holding the last command must score zero motion skill. If either self-check fails, stop; do not publish the model comparison.

Compare the same model on training and held-out episodes. A large gap signals memorisation even when loss keeps falling.

## Three misleading metrics we corrected

| Earlier measure | Problem | Current interpretation |
| --- | --- | --- |
| Motion skill including an idle arm | Holding is perfect, so the ratio can diverge | Exclude idle arm groups |
| Grasp-position ratio against hold | The demonstrator stops before grasping; hold error is tiny | Report absolute degrees |
| Timing averaged over one second | Mixes imminent grasps with difficult long-lead predictions | Also report ≤0.3 s lead time |

Keep the metric revision with each result. The earlier practice-data table used a grasp-position skill ratio; the real-data results use absolute error. They must not be read as the same scale.

In the first ACT run, training timing was 26% overall but 75% at short lead. SmolVLA later learned the training switches fully, including long lead times. That closed the question of whether the signal itself could support learning; it did not establish task generalisation.

## What the comparisons can establish

Public practice data validates the workflow, not TRON 2 model quality. Unequal training budgets, different camera sets and two held-out episodes prevent a clean architecture comparison. See the [dated results](../projects/experiments/2026-09-29-real-data.md).

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 7, 10, 10a and 10b.
