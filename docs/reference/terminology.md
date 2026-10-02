# Terminology

| Term | Meaning in this project |
| --- | --- |
| LeRobot | Dataset/training framework used for our physical imitation-learning route |
| ACT | Action Chunking Transformer; learns chunks from demonstrations |
| SmolVLA | Pretrained vision-language-action model fine-tuned on our recordings |
| OpenPI / tron2_openpi | Policy-serving/training family used by the supplied LimX checkpoints |
| FluxVLA | Separate LimX framework; its checkpoint/runtime conventions differ |
| State | Observation of the robot; gripper fields in our recordings copy commands |
| Action | Target the policy predicts; its recorded meaning must be checked |
| Chunk / H | Number of predicted future actions |
| Execution horizon / s | Number of actions used before a fresh prediction in the shared client |
| RTC | Real-time chunking fields/steering; wire compatibility is not proof the model uses steering |
| Bridge | Edubox service supplying camera observations |
| servoj | Continually published joint-target stream |
| movej | Joint-motion request whose behaviour depends on mode |
| Rest route | Measured waypoints avoiding a direct path through the table |
| Start pose | Policy-specific state reached before inference |
| Warm-up | Initial model execution before readiness |
| Watchdog | Client-side timeout that initiates controlled fault handling |
| Hold baseline | Repeat the last command, used to test evaluation |
| Oracle | Recorded actions used as the evaluator's perfect-reference check |
| Open-loop | Evaluate on recorded observations without acting on the robot |
| Generalisation | Successful behaviour beyond the training demonstrations |
| Sim2real | Transfer from simulated training to physical hardware |

[Joint layouts](joint-layouts.md) give the exact indices and units. [Source register](document-sources.md) identifies the records behind these definitions.
