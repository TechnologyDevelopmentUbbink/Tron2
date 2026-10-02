# Policy servers

The server turns a complete observation into an action chunk. It never commands the robot directly.

| Family | Framework / format | Server role |
| --- | --- | --- |
| Own ACT/SmolVLA | PyTorch; configuration + safetensors | LeRobot adapter, measured on the Spark |
| LimX policies | JAX/orbax; parameters + assets | OpenPI server behind the local policy wrapper |

The own-model package is about 0.9 GB in the recorded setup; the listed LimX checkpoints are about 12.4 GB each. These are checkpoint sizes, not GPU-memory requirements.

## Shared wire contract

The client sends state, camera images and prompt over WebSocket/msgpack. The recorded own-model server accepts 18 state values and three named images; it returns 50 × 18 actions for SmolVLA. Horizon and dimensions are model-dependent.

Metadata must identify the selected policy and report compatible dimensions. Integration also required `rtc_enabled` and `raw_actions`: adding only one produced a client failure. Accepting RTC request fields does not imply the model performs RTC steering; the measured adapter ignores those fields while the client merges chunks.

## Preprocessing and normalisation

The tested LeRobot 0.6.1 call order is preprocessor → predict action chunk → postprocessor. The postprocessor receives the action tensor directly. Wrapping it in a dict produced an action-type error.

Load the checkpoint's own normalisation. Match training camera selection and image transforms. The banana OpenPI run skipped missing normalisation statistics; that is historical behaviour, not an instruction for an own-trained model.

## Warm-up and latency

The first inference took roughly 600–1,100 ms; warmed SmolVLA inference on the Spark was about 95–98 ms. The real session reported 108 ms end to end. A server must warm up before reporting ready so the first live request does not exhaust the action queue.

At 30 fps with ten executed actions per refresh, the nominal budget is 333 ms. Distinguish model time, server time and total client round-trip time.

## Recorded own-model action guards

| Guard | Recorded setting |
| --- | --- |
| All-zero state | Refuse inference |
| First-action distance from current pose | 0.10 rad |
| Per-step arm/head change | 0.05 rad, equivalent to 1.5 rad/s at 30 fps |
| Physical joint limits | Matching joint specification; elbow limit includes the documented 15° bound |
| Gripper range | 0–0.94; exclude grippers from angular per-step limiting |

Gripper values are dimensionless opening fractions. The demonstrated open/close commands jump in one frame; a 0.05 per-step cap would smear the grasp over nineteen frames.

These are tested deployment settings, not a collision guarantee or a general robot safety rating. The LimX wrapper's corresponding behaviour remains to be verified in its new implementation.

**Source:** [UBB-IL-001](../reference/document-sources.md), section 14; [UBB-CLIENT-001](../reference/document-sources.md), section 16.3; [UBB-POL-001](../reference/document-sources.md), sections 17.1, 17.2 and 17.4.
