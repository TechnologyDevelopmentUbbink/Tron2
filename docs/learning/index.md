---
hide:
  - toc
---

<div class="wiki-header" markdown>

<p class="wiki-eyebrow">TRON 2 / SOFTWARE / LEARNING</p>

# Imitation learning

Teach the ring task from demonstrations recorded on the real TRON 2. Follow the checks before committing to a long training run.

</div>

<div class="wiki-grid" markdown>

<div class="wiki-tile" markdown>

:material-cog-outline:{ .wiki-tile__icon }

### [Set up LeRobot](lerobot-setup.md)

The working GB10 environment and how to verify GPU and video decoding.

</div>

<div class="wiki-tile" markdown>

:tron-vr:{ .wiki-tile__icon }

### [Record demonstrations](demonstrations.md)

Task consistency, cameras, variation and what a recording actually contains.

</div>

<div class="wiki-tile" markdown>

:material-checkbox-marked-circle-outline:{ .wiki-tile__icon }

### [Check & clean data](dataset-quality.md)

Zero frames, statistics, missing videos and format conversion.

</div>

<div class="wiki-tile" markdown>

:material-play-box-outline:{ .wiki-tile__icon }

### [View recordings](dataset-viewer.md)

Inspect images and joint curves together in Rerun.

</div>

<div class="wiki-tile" markdown>

:tron-learning:{ .wiki-tile__icon }

### [Train ACT or SmolVLA](act-and-smolvla.md)

Shared splits, camera mapping, monitoring and measured runtimes.

</div>

<div class="wiki-tile" markdown>

:material-chart-line:{ .wiki-tile__icon }

### [Evaluate & test](evaluation.md)

Compare held-out behaviour, then measure task success with robot trials.

</div>

</div>

The [first real-data results](../projects/experiments/2026-09-29-real-data.md) showed memorisation with four training episodes. Training loss alone is not a reason to deploy. Continue to [Running policies](../deployment/index.md) for the runtime and [Robot trials](robot-trials.md) for task-success evidence.
