# View recordings

Use the local `bekijk` workflow to inspect camera images and labelled joint curves on one timeline before training.

## What a good check looks like

All selected camera frames and vector data are present. Gripper closing in the images agrees with the jump at index 7 or 15. Check the start of each episode for zero frames and inspect the transition between episodes.

The practice validation counted all 563 frames per camera in the inspected episode. The viewer check compares entity frame counts with the episode metadata rather than trusting a successful process launch.

## Rerun's welcome screen is not the dataset

Browser mode starts a data server on port 9876 and a web viewer on 9090. Opening the viewer alone can show only a welcome screen. Use the complete URL printed by the local viewer, including its `?url=` data-server parameter.

The workflow verifies a late-joining data connection and warns if no browser connects within 180 seconds. A native-window mode is also available locally.

## Stop the actual viewer

The Rerun executable in the Python environment can be a wrapper that starts a child viewer process. Stopping only the wrapper may leave the child alive. Check the remaining process before starting another session.

**Source:** [UBB-IL-001](../reference/document-sources.md), sections 6.3, 8.8 and 10.
