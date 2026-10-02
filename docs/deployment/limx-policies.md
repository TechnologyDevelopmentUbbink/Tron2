# LimX OpenPI policies

**Owner update, 2 October 2026:** the LimX shortcut is built but untested. Earlier notes saying “specified, not built” are superseded. Implementation completion does not establish successful hardware operation.

## Model catalogue from the supplied record

| Policy | Checkpoint | State dim | Horizon | Documented task |
| --- | --- | --- | --- | --- |
| cloth | `cloth_h30_rtc_74999` | 16 | 30 | Fold a T-shirt |
| sort | `sort_h50_rtc_30000` | 18 | 50 | Sort fruit; head moves |
| candy | `candy_h30_rtc_25000` | 16 | 30 | Task text not recorded here |
| banana | `banana_h30_rtc_14999` | 16 | 30 | Ran locally in August |
| beans | `beans_h30_rtc_15000` | Not documented | 30 | Not documented |
| desktop | `desktop_h30_rtc_20000` | Not documented | 30 | Not documented |

The six policies in the source were published as `limxdynamics/tron2-openpi-models` and about 12.4 GB each. Treat this as the recorded catalogue, not a continuously updated release list.

## Shared client, policy-specific contract

The OpenPI wrapper should expose the selected policy in readiness metadata and use the shared safety client. Derive dimensions from the policy; never hard-code 18 for cloth. Keep the dimension-mismatch refusal active.

The supplied design specifies the banana start pose with head pitch about 1.05. It is about 1.95 rad from up. The connecting route has not been established as tested for LimX in the current record.

## Cell requirements recorded for cloth and sort

A 160 × 80 × 75 cm table with a pure white top, robot bracket 15 cm from the edge, head pitch 1.04 and yaw zero. Match table height, bracket position, lighting and head angle between recording and inference. Cloth additionally specifies a dark-blue size-M T-shirt in the central robot-side area.

Those requirements are task-specific. Running the model in a different cell can validate the connection chain without demonstrating the intended task.

## What needs evidence next

Verify the newly built launcher, readiness metadata, model dimensions, guards and controlled stop against the current implementation. Then test the start route and actual desktop click. Record each tested model/configuration separately; unknown beans/desktop metadata remains unknown until inspected.

**Source:** [UBB-POL-001](../reference/document-sources.md), sections 17.1 and 17.6; owner clarification 2 October.
