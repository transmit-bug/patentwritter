---
name: conversion
description: Ingestion discipline for existing materials — reads .docx / .pptx documents inline into Markdown for the disclosure interview (document-only capability, zero scripts zero dependencies). Use when the inventor supplies an existing disclosure / design description / old application / review deck and its text needs to enter the interview context. Word delivery (md → docx) is NOT this skill — that is the separately user-invoked `../word-delivery/SKILL.md`.
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# Material Ingestion Discipline (纯文档)

This skill is a **document-only capability**: docx/pptx→md is generated inline by the AI at ingestion time; no conversion script ships in the package. Probe the environment first on every ingestion, take the first available path in the degradation chain; if none is available, fail loud (state exactly what is missing) rather than pretending to have read the material.

This skill covers **ingestion only** (Stage-1 of the self-service pipeline). Producing Word deliverables from the drafts is a separate, explicitly requested step governed by `../word-delivery/SKILL.md` — never run it from here.

## Ingestion degradation chain (disclosure interview → scan existing materials)

When the inventor provides existing .docx (disclosure / design description / old application) or .pptx (review materials):

| Environment | Approach |
|---|---|
| mammoth or python-docx available | read the .docx inline → Markdown; extract images to the materials directory; text enters the interview context |
| python-pptx available | read the .pptx inline → per-slide Markdown (including speaker notes); extract images to the materials directory |
| none available | ask the inventor for text / Markdown / paste the key paragraphs directly |

Ingested materials and images land in `.patent/materials/` (see the "Workspace layout" section of patent-intake), never mixed into the application documents directory.

Ingestion output is **interview context, not a draft**: extracted text follows the extract-confirm-fill protocol in `../patent-intake/references/source-modes.md`; nothing is copied into `drafts/` (alias `草稿/`) without inventor confirmation.

## Optional dependencies

See `requirements-optional.txt` in the same directory. All "optional, install on demand": not installing means taking the degradation chain, which does not block the flow. Probe before use; no pre-installation required.

## Boundaries

- Only structured conversion of text / images / tables into interview-usable Markdown.
- `.doc` (legacy format) is not converted; ask the inventor to save as .docx or provide text.
- This skill is zero-script: any urge to "download a script / run a repo conversion tool" is out of bounds — generate inline or degrade.
- No Word delivery here: md→docx belongs to the user-invoked `../word-delivery/SKILL.md`.
