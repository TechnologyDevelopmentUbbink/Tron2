# Recording demonstrations

Our proof-of-concept task is to pick up a red ring and place it in the red bin. Physical demonstrations are recorded through the PICO teleoperation workflow; see [Controller & VR](../hardware/controller.md#vr-teleoperation).

## Keep the task and observations consistent

Record the task instruction, camera identities, frame rate and joint layout with the dataset. Vary useful task conditions deliberately: object position, approach and starting arrangement. A handful of near-identical episodes is useful for checking the pipeline, but does not establish generalisation.

Check the export against what was recorded. The first real export had six episodes; two expected recordings were missing.

## What the files contain

The tested LeRobot 0.6.1 workflow uses v3.0:

| Path | Purpose |
| --- | --- |
| `meta/info.json` | Format, frame rate, features and file paths |
| `meta/stats.json` | Normalisation statistics |
| `meta/tasks.parquet` | Task instructions |
| `meta/episodes/…parquet` | Episode boundaries and data/video file mapping |
| `data/…parquet` | States and actions, with multiple episodes per file |
| `videos/<camera>/…mp4` | Camera streams, with multiple episodes per file |

Our default state/action layout has 18 values. Grippers are at indices 7 and 15, head pitch/yaw at 16 and 17. See the [exact layout](../reference/joint-layouts.md).

The first recordings contain five cameras. The deployed own-model chain uses three. Camera selection and preprocessing must match the model; do not assume every recorded stream reaches inference.

## State is not always a measurement

Arm state is measured joint position. In the checked recordings, gripper state is an exact copy of the gripper command, including the frame of a jump. It does not report whether the jaws actually closed.

The public practice dataset had action approximately equal to measured state. That must not be generalised into a claim about our TRON 2 arm recordings: the checked arm values were not exact copies. A recorder source audit remains a separate provenance question.

## Before training

1. [Check the export](dataset-quality.md), including all cameras for each episode.
2. [View it](dataset-viewer.md): check that visual gripper motion agrees with the curves.
3. Preserve the original. Work from a validated clean copy when a supported repair is necessary.
4. Save one train/test split and use it for both architectures.

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 4, 8 and 10a.
