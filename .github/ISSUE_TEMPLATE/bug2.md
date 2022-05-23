name: "\U0001F41E Bug"
description: Create a report to help us improve
title: "[Bug]: "
labels: ["bug", "triage"]
assignees:
  - codervinod
body:
body:
  - type: markdown
    id: general
    attributes:
      value: |
        Thank you for reporting an issue. Before you open the bug report please review the following troubleshooting guide:
          - [Troubleshoot RapidFort Community Images Issues](https://github.com/rapidfort/community-images/blob/main/TROUBLE_SHOOTING.md)

        Please fill in as much of the following form as you're able.
  - type: input
    id: affected_image
    attributes:
      label: Image name
      description: Name of the affected image (repository+tag)
      placeholder: rapidfort/postgresql:latest
    validations:
      required: true
  - type: checkboxes
    id: runtime
    attributes:
    label: Which runtime are you using to reproduce this issue?
    description: You may select more than one.
    options:
      - label: Kubernetes
      - label: Docker Compose
      - label: Docker
  - type: dropdown
    id: non_hardened_reproducible
    attributes:
    label: Is this issue reproducible on the original non-hardened image?
    description: Please select one
    options:
      - label: Yes
      - label: No
  - type: dropdown
    id: bug_type
    attributes:
    label: Could you please review our troubleshooting (/TROUBLE_SHOOTING.md) guide and identify the category?
    description: Please select one
    options:
      - label: Coverage Script
      - label: RF Hardening
      - label: Source image usage
      - label: Source image behavior
      - label: Unknown
  - type: textarea
    id: steps
    attributes:
      label: What steps will reproduce the bug?
      description: Enter details about your bug.
      placeholder: |
        1. In this environment...
        2. With this config...
        3. Run '...'
        4. See error...
    validations:
      required: true
  - type: textarea
    id: custom_params
    attributes:
      label: Are you using any custom parameters or values?
      description: Add any parameter used via `--set` or as a `values.yaml` customization.
  - type: textarea
    id: expected_behavior
    attributes:
      label: What is the expected behavior?
      description: If possible please provide textual output instead of screenshots.
  - type: textarea
    id: actual_behavior
    attributes:
      label: What do you see instead?
      description: If possible please provide textual output instead of screenshots.
    validations:
      required: true
  - type: textarea
    id: more_details
    attributes:
      label: Additional information
      description: Tell us anything else you think we should know.