# movej accepted without motion

**Symptom:** movej is accepted without an error, but the pose does not change and arrival times out. A success-like “init pose reached” log is not sufficient.

**Observed context:** Advanced Developer Mode with High-Level active, 30 September. This is a mode-specific finding, not a claim that movej never works.

**Working path:** the measured route uses command_joints through the same servoj stream as policy execution, with arrival checked against state feedback. Grippers remain separate. Do not change modes in the middle of fault recovery.

The original banana client is unsuitable for this diagnostic because its failure/stop paths can drop the arms. Use the current safety client and a controlled test.

[Route design](../deployment/startup-and-rest.md) · [Command dimensions](../reference/joint-layouts.md) · [Evidence](../projects/experiments/2026-09-30-deployment.md).

**Source:** UBB-IL-001 section 15.3 and UBB-CLIENT-001 section 16.8, [source register](../reference/document-sources.md).
