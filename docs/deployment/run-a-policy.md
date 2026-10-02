# Start and stop a policy session

This is the measured own-model workflow. The LimX shortcut is built but has not yet been tested; see [LimX policies](limx-policies.md).

## Before starting

- Robot in the post-`L1+X` initial state, with arms hanging.
- Advanced Developer Mode with High-Level active.
- Compliance control active.
- Space in front clear; nobody within reach of arms or head.
- An operator at the emergency stop.
- No simultaneous training or second GPU policy server.

Confirm the setup still matches the measured cell and calibration. A recorded route is specific to that cell.

## Select, validate and wait

Use the own-model shortcut or its locally maintained command-line equivalent. Select the policy by name. The launcher validates weights, task text, camera count and configuration before starting.

The server warms up before reporting **GEREED**. The client checks that the expected policy is ready; a listening port alone is insufficient. Read the checklist and confirm **JA** before anything moves.

Both logs are visible, side by side with tmux where available. The local launcher also supports separate windows.

## What happens next

The client follows the [measured rest/startup route](startup-and-rest.md), verifies arrival at the policy's start pose, then enables inference. A failed arrival returns to rest and ends the session without querying the policy.

## Normal stop

Use `Ctrl+C` in the client and let the route finish. Do not close the window. Do not pipe the client through `tee`: a stopped pipe can break output during the return route.

Software brings the robot to rest. Motor release is a separate manual action using `L1+X`; do not substitute a motor-cut emergency stop for controlled fault recovery.

## If the rest route fails

The client holds position and reports the failure rather than exiting. Use the documented manual controller action, then the client's two-`Ctrl+C` override within three seconds. A single interrupt during the route is ignored with a message.

A power cut, hard process crash or lost robot command connection cannot be made safe solely by these watchdogs. The operator and physical setup remain part of the procedure.

**Source:** [UBB-POL-001](../reference/document-sources.md), sections 17.2–17.5 and 17.7. The actual desktop click remains unverified in the supplied record.
