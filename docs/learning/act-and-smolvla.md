# Train ACT and SmolVLA

Use a short pipeline test on each new dataset before a full training run. The local training utilities manage splits and checkpoints; their implementation is maintained outside this wiki.

## Shared rules

Both architectures use the same complete episodes and held-out split: the last 20%, with at least two test episodes. Save the split alongside the run. Comparing models from different datasets or test sets is refused by the local evaluator.

| Setting | ACT | SmolVLA |
| --- | --- | --- |
| Initial weights | From scratch | Fine-tune `lerobot/smolvla_base` |
| Full run | 20,000 steps, batch 8 | 20,000 steps, batch 32 |
| Short pipeline run | 3,000 steps | 1,400 steps |
| Full-run checkpoint interval | 5,000 | Follow the recorded run configuration |
| Predicted chunk | 100 actions | 50 actions |
| Cameras | Selected features; first real run used five | Three, mapped to `camera1..3` |

The final short-run checkpoint is saved. Compare training-episode and test-episode results before spending another night training.

## Cameras must match deployment

SmolVLA takes one overview camera, then left and right wrist cameras. A naive stereo-head mapping selected both head images and dropped a wrist; the explicit mapping avoids that error.

The first five-camera ACT model does not fit the deployed three-camera chain and is refused by the policy launcher. The deployed model's image selection, resolution and transforms must agree with training.

A fine-tuned SmolVLA config retained an input shape of six from the base model. Changing other state dimensions changed its predictions, proving the tested model used more than that metadata suggests. Do not infer runtime vector compatibility from this field alone; the live client/server dimension check remains required.

## Monitoring

TensorBoard runs locally, with the recorded workflow using port 6007. The LeRobot 0.6.1 logger adapter produced values matching the training log. It is tied to that release and needs rechecking after an upgrade.

## Recorded runtimes on GB10

| Model / cameras | Measured rate | Short/full time |
| --- | --- | --- |
| ACT batch 8 / 3 | 0.42 s/step, 800-step run; 8.3 GB | 3,000 ≈21 min; 20,000 ≈2.3 h, extrapolated |
| ACT batch 8 / 4 | 0.59 s/step, 500-step run | 3,000 ≈30 min; 20,000 ≈3.3 h, extrapolated |
| ACT batch 8 / 5 real cameras | 0.85 s/step; 13.7 GB | **3,000 =42.5 min measured**; 20,000 ≈4.7 h |
| SmolVLA batch 32 / 3 | 1.36 s/step, 400-step run; 10.7 GB | 1,400 ≈32 min; 20,000 ≈7.5 h, extrapolated |

Run long jobs sequentially. Shared GPU load increased time per step substantially.

## Training loss is not the verdict

ACT's L1/KL loss and SmolVLA's flow-matching loss are not comparable scores. Low loss can also accompany memorisation. Use [Evaluation](evaluation.md), then [Robot trials](robot-trials.md).

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 5–7, 8.8 and 10a–10b.
