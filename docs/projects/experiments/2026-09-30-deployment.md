# 30 September — server, routes and fault tests

The server was built/measured on the Spark, the rest route exercised on the real robot, and client fault handling subsequently tested against a mock robot/Bridge/network with the real SmolVLA server.

## Environment and serving

The same package environment transferred to the Spark and reproduced the home evaluation numbers: 6.0° arm error, 50% timing hits overall and 67% short-lead. Cached SmolVLM files allowed offline model loading.

| Measurement | Result |
| --- | --- |
| Warmed Spark SmolVLA | Median 95 ms, p95 97 ms; 3 ms spread |
| GX10 SmolVLA | Median 104 ms, p95 109 ms |
| Earlier banana policy | 186–190 ms model; 261–267 ms server; 263–270 ms end to end |
| Own-model first protocol call | About 711 ms |
| Launcher warm-up | 605 ms, then 98 ms; first real request 108 ms |

At 30 fps and s=10, 333 ms is available per refresh. Model latency and refresh cadence are different measures.

## Integration corrections

Local checkouts were nearly unchanged: OpenPI dependency versions and banana configurations differed; tron2_env had added Bridge scripts. There was no layout.py in the inspected checkout. State dimension simply truncated the vector, and conversion already included head targets for 18-dimensional actions.

The first LeRobot postprocessor call used the wrong wrapper type. Missing WebSocket packages also surfaced: `websocket-client` and `websockets` are distinct dependencies; `msgpack` is required by the protocol. The uv-created environment did not contain pip.

The client/server combination needed both `rtc_enabled` metadata and `raw_actions`. These requirements were discovered by testing the combination, after the server-alone tests passed.

## Limits and real observations

Arm p99 per-step changes were 0.018–0.044 rad; head 0.024–0.031 rad. Gripper p99 change was 0.19 opening fraction, max 0.94. Large angular maxima at episode boundaries/zero frames were not treated as normal physical movement.

Random images caused 102 clipped values and were misleading. A real dataset observation produced 26 clipped values out of 900; first action distance 0.024 rad and largest step 0.033 rad. Tests also refused zero state and wrong dimensions and accepted RTC fields.

## Measured route and start pose

Three waypoints were recorded by hand. movej accepted requests without motion in the active mode; command_joints worked. Timing changed from 3/3/4 to 6/6/8 seconds.

First-chunk clipping for candidate starts:

| Candidate | Clipped values of 900 |
| --- | --- |
| Frame 0 of episode 1 | 11–36 across the six episode image sets |
| Mean/median across episodes | About 60 |
| Banana start | About 133 |
| Rest | About 211 |
| Up | About 325 |

One real recorded pose was selected. The final-leg speed calculation corrected the mistaken idea that a fixed ten seconds was necessarily slow.

## Mock fault matrix

| Scenario | Observed response |
| --- | --- |
| Normal end, server killed, Ctrl+C | Rest route |
| Network interruption to inference | Warn at 1 s; rest at the 10 s threshold |
| Image conversion error | Rest route |
| Wrong server state/action dimension | Refused before incompatible execution |
| Bridge stalled | Rest after 5 s |
| Start pose 0.649 rad off | Rest and stop; no policy query |
| Already at rest | Initial rest route skipped |
| 0.25 rad off rest | Full route |
| Rest route failed | Hold with stream alive; manual two-interrupt override |
| Missing JA, wrong policy on port, closed server window | Refused |
| Original client / server killed | Simulated arms dropped after 1 s |

The negative control demonstrates that the rig detects the failure. A test-log indexing mistake was fixed and the figures rechecked; affected older logs carried a warning.

## Historical proposal

The earlier plan reused the banana protocol and replaced its model server instead of building a new LeRobot robot plugin. The later work also changed the safety client, corrected its placement and added readiness fields. Keep the proposal's assumptions distinct from the measured design.

The source records local commits a8f6669/254b79a for server/limits and 67c52fb/6437e23 for the route. Their code repository is not published here.

**Source:** [UBB-IL-001](../../reference/document-sources.md), sections 13–15 and appendix; [UBB-CLIENT-001](../../reference/document-sources.md), section 16; [UBB-POL-001](../../reference/document-sources.md), section 17.7.
