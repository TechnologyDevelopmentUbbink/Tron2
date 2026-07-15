# Source Classification

Use a classification label whenever a page introduces technical information. Place the label near the relevant statement or section, and record traceable sources wherever possible.

## Official source

Information taken directly from LimX Dynamics documentation. Include the document title, version, and page or section where possible.

!!! success "Official source"

    **Source:** _Document title_, version `[version]`, section `[section]` or page `[page]`.

    Replace this example with an accurate summary after the source has been reviewed.

## Ubbink verified

Information tested and confirmed on the physical TRON 2 owned by Ubbink. Record the relevant software, firmware, hardware revision, test conditions, and reviewer when available.

!!! tip "Ubbink verified"

    Verified on the Ubbink TRON 2 under the conditions recorded here. Add reviewer and version evidence before using this label.

## Practical observation

Behavior observed during use but not yet formally verified. Describe the context without presenting the observation as a guaranteed result.

!!! note "Practical observation"

    This behavior was observed during practical use and still requires controlled verification.

## Unverified

Translated, incomplete, uncertain, or not yet tested information. Keep this label visible until a reviewer can validate the content.

!!! warning "Unverified"

    This information has not been verified. Do not rely on it for safety-critical or equipment-critical decisions.

## Version dependent

Information that may change depending on firmware, SDK, ROS package, or hardware revision. State all known applicable versions and avoid implying compatibility beyond the evidence.

!!! info "Version dependent"

    Confirm the applicable firmware, SDK, ROS package, and hardware revision before using this information.

## Applying labels

1. Select the strongest label supported by current evidence.
2. Add a source citation or verification record.
3. Keep uncertain translations marked **Unverified**.
4. Add **Version dependent** alongside another label when compatibility may vary.
5. Update the page status and revision history after review.
