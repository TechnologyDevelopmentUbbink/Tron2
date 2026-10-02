# Firmware and calibration

**Owner confirmation, 2 October 2026:** firmware and joint zeroing have not changed since the measured routes and recordings.

## Record the installed set

Record controller, onboard services, SDK/runtime and application versions together. The supplied notes mention a complete update set available from 24 September; they do not establish which versions are currently installed.

## Re-zeroing changes the reference

The client supplement reports that a main-controller upgrade requires joint re-zeroing. If that occurs, previously measured poses no longer share the same encoder reference. Re-measure startup/rest waypoints and reassess recordings and model start poses before reusing them.

Verify the requirement for the actual update set. Availability of an update is not evidence that it has been applied.

## After a change

Record before/after versions and calibration status. Repeat read-only layout/state checks, then validate the route and fault paths in the current cell. Keep previous measurements as historical evidence rather than silently replacing their context.

Follow the matching official update/calibration instructions; this page does not supply an invented recovery procedure.

**Source:** [UBB-CLIENT-001](../reference/document-sources.md), section 16.8; owner confirmation 2 October.
