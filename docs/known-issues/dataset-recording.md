# Recording and normalisation problems

**Symptoms:** all-zero state at episode start, unexpectedly huge loss, missing video during training, or suspiciously constant gripper channels.

Inspect data and metadata together. The first export contained five zero-state rows and incorrect zero standard deviations on two moving action channels. A partial practice dataset's advertised episode count also exceeded its video-complete episodes.

The validated local clean-copy route fills only short stationary gaps and recomputes statistics while preserving video alignment. The recorder root cause remains unresolved; repairing a copy does not establish that the source is fixed.

Do not choose a gripper channel solely by name. In the practice data the named channel was dead and motion was in finger joints. In TRON 2 recordings, gripper observation copies command rather than measured closure.

[Dataset checks and limits](../learning/dataset-quality.md) · [Recording semantics](../learning/demonstrations.md).

**Source:** UBB-IL-001 sections 8 and 10a, [source register](../reference/document-sources.md).
