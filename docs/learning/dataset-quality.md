# Check and clean a dataset

The local `controleer` utility reports ready, usable with understood warnings, or **NIET TRAINEN**. Do not bypass a failed check to see whether training happens to run.

## Checks that prevent silent errors

| Check | Why it matters |
| --- | --- |
| LeRobot v3.0 | The tested 0.6.1 loader rejects v2.1 |
| Complete episodes | Data alone is insufficient; every selected camera must be present |
| Joint names, order and ranges | A wrong gripper index can command another joint without a crash |
| Constant/nearly constant channels | A channel name can look correct while its data never changes |
| Gripper scale | Values are 0–1, not 0–100 |
| Zero state/arm frames | A disconnected or uninitialised observation is not a valid zero pose |
| Normalisation | A near-zero standard deviation on a moving channel amplifies tiny errors |
| Action/state lag by active group | Distinguishes measured positions from plausible command targets |
| Gripper state/command equality | Documents the feedback signal actually available to the model |

The episode count in `info.json` describes the full dataset. A partial download may contain far fewer usable episodes: the practice export had 861 episodes in its data file, but only 47 with all videos present, while metadata claimed 1,367.

## Supported repairs preserve alignment

The local clean-copy utility fixes zero-state frames and vector statistics in a copy.

- Fill from the nearest valid state in the same episode.
- Refuse gaps longer than 10 frames or command movement greater than 0.01 rad.
- Recompute vector statistics with a standard-deviation floor of 0.01.
- Preserve frame indices, global indices and video timestamps.

On the first export, exactly five rows changed and camera images remained identical. Deleting those rows would have shifted alignment. The cause of the recorder's zero frames remains unknown.

Exactly constant channels are different from moving channels with incorrectly recorded zero standard deviation. Two nearly idle right-arm action channels had real standard deviations of 1.8e-4 and 1.25e-3, but metadata said zero; the first ACT loss started at 2,838 instead of the usual 12–40.

## Older datasets

Use the copy-based v2.1-to-v3.0 conversion route. The underlying LeRobot converter operates in place, so do not apply it directly to the only original. Four sampled frames matched the official ALOHA v3.0 release; a one-frame-shift negative check detected the mismatch. This validates the sampled comparison, not every byte in the full dataset.

## Action versus measured state

If action tracks measured state without a lead, inspect the recorder and command path before using an offline score to select a model. A shifted-state approximation is an untested workaround, not established command ground truth.

Our recorded gripper command never exceeds 0.94. This does not confirm a hypothesised 95% SDK clamp: the recordings contain commands, and 0.94 is not 0.95.

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 6.2 and 8.1–8.7.
