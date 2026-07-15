# Controller and VR Headset

This page is the working structure for learning and documenting every physical control, button combination, operating state, and VR-headset interaction used with the TRON 2.

!!! danger "Not an operating instruction yet"

    The controller mappings and procedures have not been imported or verified. Do not operate the robot from this page until each action is supported by an official source or a recorded Ubbink verification.

## What this guide will cover

- Identifying the exact handheld controller and VR equipment
- Explaining every button, stick, trigger, switch, and indicator
- Documenting single-button actions and multi-button combinations
- Recording the state or mode required for each action
- Showing the expected robot and controller feedback
- Explaining how to begin, use, and end a VR control session
- Providing safe stop, recovery, and troubleshooting references

## Equipment and version record

Complete this table before adding control mappings. A different controller profile, firmware release, or headset can change the behavior.

| Item | Identified value | Evidence |
| --- | --- | --- |
| Handheld controller manufacturer and model | Not yet recorded | Not yet imported |
| VR headset manufacturer and model | Not yet recorded | Not yet imported |
| VR controller model | Not yet recorded | Not yet imported |
| Robot hardware revision | Not yet recorded | Not yet imported |
| Robot firmware version | Not yet recorded | Not yet imported |
| Controller profile or application version | Not yet recorded | Not yet imported |

!!! info "Version dependent"

    Treat every mapping on this page as version dependent. Record the tested versions with each verified control table.

## Before using a controller

The verified guide must define these conditions before any button instructions are published:

- Required operator training and approved source documents
- Suitable operating area and pre-operation checks
- How the active control mode is identified
- How the operator confirms which controller has authority
- The approved stop and emergency response references
- What to do when controller feedback differs from the documented result

See [Safety](../getting-started/safety.md), [Operation preparation](../operation/preparation.md), and [Emergency stop](../operation/emergency-stop.md). These pages are also under development.

## Handheld controller

### Annotated controller views

Add clear front, rear, and top images after the exact controller is identified. Number each physical control on the image and use the same number in the control inventory.

!!! note "Image needed"

    Store approved images under `docs/assets/images/controller/`. Remove serial numbers, account names, network details, and other sensitive information before publishing.

### Complete control inventory

Add one row for every labeled or movable control. Do not copy mappings from a similar-looking controller.

| Image no. | Printed label | Control type and location | Action | Required state | Expected feedback | Classification and source |
| --- | --- | --- | --- | --- | --- | --- |
| To be documented | To be documented | To be documented | Not yet verified | Not yet verified | Not yet verified | Unverified |

### Button combinations

Record timing and order precisely. A simultaneous press, ordered sequence, short press, and long press are different combinations.

| Combination | Exact input and timing | Required state | Intended action | Expected feedback | Abort or recovery | Classification and source |
| --- | --- | --- | --- | --- | --- | --- |
| To be documented | Not yet verified | Not yet verified | Not yet verified | Not yet verified | Not yet verified | Unverified |

### Indicators and feedback

| Indicator, sound, or vibration | Pattern | Meaning | Operator response | Classification and source |
| --- | --- | --- | --- | --- |
| To be documented | Not yet verified | Not yet verified | Not yet verified | Unverified |

## VR headset and VR controllers

### Scope and equipment

This section will describe the specific supported headset, its hand controllers, the robot-side software involved, and the limits of the verified configuration. It must not assume that another headset or application behaves the same way.

### VR control map

Create separate annotated images for the left and right VR controllers and add every physical input to this table.

| Hand | Printed label or image no. | Input | Action | Required state | Expected feedback | Classification and source |
| --- | --- | --- | --- | --- | --- | --- |
| To be documented | To be documented | To be documented | Not yet verified | Not yet verified | Not yet verified | Unverified |

### VR button combinations

| Combination | Left-hand input | Right-hand input | Timing | Required state | Intended action | Classification and source |
| --- | --- | --- | --- | --- | --- | --- |
| To be documented | Not yet verified | Not yet verified | Not yet verified | Not yet verified | Not yet verified | Unverified |

### Start a VR session

1. **Prerequisites:** not yet imported or verified.
2. **Prepare the headset and application:** not yet imported or verified.
3. **Connect to the robot:** not yet imported or verified.
4. **Confirm control authority and mode:** not yet imported or verified.
5. **Verify feedback before movement:** not yet imported or verified.

### End a VR session

1. **Return the robot to the approved state:** not yet imported or verified.
2. **Release VR control authority:** not yet imported or verified.
3. **Disconnect or close the application:** not yet imported or verified.
4. **Record unexpected behavior:** not yet imported or verified.

## Procedure template for each action

Use this structure when a control action is added:

1. Name the intended outcome.
2. State all prerequisites and the required robot/control mode.
3. Identify the exact controller and applicable versions.
4. Describe the input, order, and timing.
5. Describe expected controller, application, and robot feedback.
6. Explain how to stop or abandon the action safely by linking to an approved procedure.
7. Record the source classification and evidence.

??? example "Example record structure - no real mapping"

    **Action:** `[descriptive action name]`
    **Required state:** `[verified state]`
    **Input:** `[exact button or combination and timing]`
    **Expected feedback:** `[verified visible, audible, or physical response]`
    **Applicable versions:** `[hardware, firmware, application, and controller profile]`
    **Source:** `[official document and section, or Ubbink verification record]`

## Troubleshooting

Until verified diagnostics are available, record the following without exposing confidential information:

- Exact equipment models and relevant versions
- Robot and controller state before the problem
- Exact input sequence and timing
- Visible indicators and application messages
- Whether the behavior can be reproduced
- Changes made since the last known working session

See [Connection problems](../troubleshooting/connection-problems.md), [Software problems](../troubleshooting/software-problems.md), and [Diagnostic information](../troubleshooting/diagnostic-information.md).

## Sources

No controller or VR source material has been imported yet. When sources become available, record document title, version, language, page or section, and redistribution restrictions in [Document sources](../reference/document-sources.md).
