---
tags:
  - ROS
  - Bridge
  - limx-agent
---

# rospy.init_node() ordering breaks the Bridge

**Symptom**

A script combining `tron2_env.bridge.BridgeObservationProvider` with `rospy` hangs forever waiting for observations — no error, just an infinite, misleading timeout loop.

**Cause**

`rospy.init_node()` was called *before* `BridgeObservationProvider.start()`. Calling it first silently breaks the asyncio event loop the Bridge provider depends on. This is hard to spot because there's no exception — the script just never produces output. Isolated by stripping the script down to bare Bridge-only code (worked every time) versus the full script with rospy (never worked), then reordering the two calls.

**Fix**

Call `BridgeObservationProvider.start()` **first**, then `rospy.init_node()` after.

**Related pitfalls in the same bridge script**

- `BridgeConfig(host=...)` needs the `wss://` scheme — `host='10.192.1.4'` alone silently produces no connection; must be `host='wss://10.192.1.4'`.
- `BridgeConfig(joint_topics={})` is required — by default the Bridge waits to align image *and* joint topics before releasing any observation, but TRON2's joint state doesn't flow through the Bridge at all (it's a separate direct robot WebSocket). Without disabling joint subscription, the aligner waits forever.
- `get_joint_states()` returns a dict with keys `timestamp`, `robot_timestamp`, `states`, `joint_updated`, `gripper_updated` — only `states` (a flat list of 18 floats) is the actual joint data. Using `dict.values()` directly mixes in non-numeric fields and silently breaks `JointState.position`.
- To verify the pipeline is actually working, don't trust `rospy.get_master().getSystemState()` with this lightweight `rospy` build (returns empty results even when the pipeline is fine) — subscribe to the topics directly in a second terminal and confirm messages are arriving.

**Related**

- Source: build log, Aug 28 (not yet migrated into the wiki as its own page)
