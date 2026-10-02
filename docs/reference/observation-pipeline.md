# Observations and action playback

The client forms an observation from two independent streams: images from the Edubox Bridge and joint state from the robot controller.

## Stream contract

| Stream | Recorded path | Context |
| --- | --- | --- |
| Overview image | Bridge, `cam_high` | 640 × 480 in the supplied diagram |
| Wrist images | Bridge, `cam_left_wrist` / `cam_right_wrist` | Two 848 × 480 streams in the supplied diagram |
| Joint state | Direct control WebSocket | 200 Hz readout; 18-value state |
| Aligned observation | Client → policy server | State, three images and task prompt |
| Actions | Policy server → client | Model-dependent horizon and dimensions |
| Joint targets | Client → robot controller | Interpolated 300 Hz servoj stream |
| Gripper targets | Separate controller API | Opening fraction converted to percent |

The client aligns camera and state timestamps within 200 ms. This is a maximum alignment tolerance, not an additional 200 ms inference delay. A responsive controller with no images cannot form a complete observation.

Bridge configuration must use the secure WebSocket scheme and disable Bridge joint topics when joint state arrives directly. See [Bridge pitfalls](../known-issues/ros-bridge-init-order.md).

## Training and inference images

The five recorded cameras are not automatically the three deployment cameras. Explicitly choose overview, left wrist and right wrist. The earlier OpenPI client resized/padded to 224 × 224; the measured LeRobot deployment uses the model's matching preparation. Record transforms with the selected model; do not silently apply a different route's defaults.

## Predicted chunk versus executed actions

ACT predicts 100 actions and SmolVLA 50 in the recorded training setup. The client decides how much of each chunk to execute before refreshing; the measured session used **s=10/H=50**.

At 30 fps, ten executed actions represent about 0.33 seconds, so nominal refresh cadence is about **3 Hz**. This is separate from approximately 95 ms model inference and 300 Hz joint-target publication.

The standalone LeRobot `n_action_steps` setting also controls playback and can be changed without retraining. In our shared deployment chain, refresh is controlled by the client's execution horizon; the queue requests another chunk at H−s and merges old/new actions. Do not assume changing a standalone model setting alone changes the client schedule.

ACT temporal ensembling is a separate option: configure it when loading, with one action step, and measure its smoothing/latency effects. It was not established as the best ring-task setting.

**Source:** [UBB-IL-001](document-sources.md), sections 12–14; [UBB-POL-001](document-sources.md), section 17.8 and accompanying diagram.
