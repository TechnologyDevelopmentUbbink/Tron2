# 28 September — environment and practice data

**Context:** ASUS Ascent GX10, GB10/aarch64, 128 GB unified memory. The [working package set](../../learning/lerobot-setup.md) passed CUDA and AV1 decoder checks, including a deliberate one-frame-shift negative check.

## Practice dataset

UBTECH Packing_Box simulation data was converted into an 18-dimensional practice layout. It is not TRON 2 data. A partial download yielded 47 complete episodes (833 MB); the default test split was 38 training and 9 test.

The inspected episode exposed all 563 camera frames and joint/action curves. Constant head, a dead gripper state channel and action≈state were properties of the source, correctly flagged.

## Earlier evaluator results

| Model | Training | Timing hits | False alarms | Grasp skill (old metric) | Motion skill |
| --- | --- | --- | --- | --- | --- |
| Oracle | Self-check | 100% | 0% | +1.00 | +1.00 |
| Hold | Self-check | 0% | 0% | 0.00 | 0.00 |
| ACT | 30 steps, pipeline test | 8% | 1% | −0.64 | −0.51 |
| ACT | 800 × batch 8 | 38% | 0% | +0.28 | +0.41 |
| SmolVLA | 400 × batch 32, pretrained | 100% | 0% | +0.84 | +0.79 |

There were 108 gripper switches across the test episodes. Median timing error among hits was 0.13 s for ACT and 0.07 s for SmolVLA. The source identifies evaluation output `beoordeling_2026-09-28_2244.json`; raw output is not distributed here.

The old grasp metric was subsequently replaced with absolute degrees. Do not compare it directly with the next day's table.

## Interpretation

The workflow can discriminate a minimally trained model from a longer run and passes oracle/hold checks. It cannot establish which architecture is better on TRON 2: action≈state, another robot, synthetic gripper conversion, unequal short training and open-loop evaluation all limit the result.

A separate ALOHA v2.1 conversion matched four sampled state/action/image frames in the official v3.0 release. The shifted-frame negative comparison failed as intended.

**Source:** [UBB-IL-001](../../reference/document-sources.md), sections 3, 6, 8.3 and 10.
