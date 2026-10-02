# Startup and the measured rest route

A safe-looking rest pose is not enough: a straight path from a working pose can cross the table. The route is specific to our cell.

## Three measured waypoints

The operator positioned the robot by hand; a read-only script recorded all 18 values for up, rotated and rest. They were measured, not invented from a drawing.

The return path is **up → rotated → rest**. The first 3 + 3 + 4 second test was too quick to monitor comfortably; the route was changed to 6 + 6 + 8 seconds. The command sets a destination; state feedback verifies each arrival.

Do not reuse LimX's straight-to-init movement in this cell. Do not overwrite a recorded waypoint silently by reusing its name.

## Use the command path that works in the active mode

In Advanced Developer Mode with High-Level active, the tested `movej` call was accepted but did not move the robot. The route uses `command_joints` through the same 300 Hz servoj stream as the policy. See [Accepted without motion](../known-issues/movej-no-motion.md).

## Startup sequence

1. Return along the rest route, unless already within the rest threshold.
2. Reverse through rest → rotated → up.
3. Move slowly to the selected policy's start pose.
4. Verify arrival within 0.15 rad.
5. Only then enable the policy.

The recorded rest-skip threshold is 0.20 rad over arms/head, excluding grippers. Settings above 0.30 rad are refused. Skipping saved about 24 seconds, reducing the reported startup from 63 to 39 seconds.

For the final leg, use the larger of 10 seconds and distance / 0.2 rad/s. A 4.63 rad move therefore takes about 23 seconds. A fixed ten-second duration would be faster than the route. The earlier supplement records rejecting configured maximum speed at or above 0.29 rad/s.

## Choose a real policy start pose

The tested own-model choice was frame 0 of a real episode, stationary for 31 frames. It clipped fewer predicted values than an averaged pose, the banana start, rest or up. A mean pose may never have occurred during recording.

A start-state choice does not prove the connecting path is clear. The own-model sequence was subsequently exercised in the 1 October session. The LimX path and shortcut still require their own test.

The inspected recording had a wrist 0.0006 rad beyond its limit. The client reports and clamps discrepancies up to 0.01 rad; larger violations are refused.

## Calibration changes invalidate the reference

The owner confirms no firmware/re-zero change as of 2 October. If joint zeroing changes later, remeasure waypoints and reassess the dataset/model relationship before reusing them. [Firmware and calibration](../software/firmware.md).

**Source:** [UBB-IL-001](../reference/document-sources.md), section 15; [UBB-CLIENT-001](../reference/document-sources.md), sections 16.4–16.5; [UBB-POL-001](../reference/document-sources.md), sections 17.3 and 17.7.
