# PRD.md — Playlytics V3
# Product Requirements Document

---

## Project Identity

**Product Name:** Playlytics V3
**Version:** 3.0.0
**Type:** Desktop Application
**Platform:** Windows (primary), cross-platform compatible
**Language:** Python 3
**UI Framework:** Tkinter
**Distribution:** Standalone executable via PyInstaller
**License:** MIT

---

## Problem Statement

Players who want to understand their in-game performance have no simple,
offline tool that gives them structured, readable feedback based on their
match statistics.

V2.9 proved the concept works but was a procedural script with no GUI,
no structured output, and no maintainability.

V3 solves this by rebuilding the analyzer as a professional desktop
application with clean architecture, structured results, and a proper UI.

---

## Target Users

**Primary User:**
A casual to semi-competitive FPS player who wants quick,
readable feedback on their match performance without needing
to interpret raw numbers themselves.

**Technical Level:**
Non-technical. The user should never see code, errors, or
raw data structures. Everything is presented in plain language.

**Secondary User:**
A developer or recruiter reviewing the codebase as a portfolio
project. They should find the code clean, documented, and
professionally structured.

---

## User Goals

- Enter match statistics quickly
- Receive clear, readable performance feedback
- Understand what they did well and what needs improvement
- Get weapon-specific analysis relevant to how they played
- Never encounter a crash or confusing error message

---

## Product Goals

- Demonstrate clean software architecture
- Demonstrate defensive programming
- Demonstrate modular design
- Demonstrate professional documentation
- Demonstrate testability
- Produce a distributable executable
- Produce a GitHub release worthy of a portfolio

---

## Core Features — V3.0.0

### Input
- Kills (integer)
- Deaths (integer)
- Accuracy (float, percentage)
- Gun type (string, selected from supported list)

### Validation
- Type checking on all inputs
- Range checking (kills 0-200, deaths 0-200, accuracy 0-100)
- Normalization (strip whitespace, lowercase)
- Alias support (ar maps to assault)
- Structured error messages on invalid input
- Application never crashes on bad input

### Analysis
- K/D ratio calculation
- Small sample detection and suppression
- General performance rules:
  - Accuracy classification
  - K/D classification
  - Positioning analysis
  - Survival analysis
- Weapon-specific analysis:
  - Sniper
  - SMG
  - Assault Rifle
  - LMG
  - Shotgun

### Output
- Structured result cards
- Each card has a severity level (SUCCESS, INFO, WARNING, ERROR)
- Card color determined by severity
- Plain language messages
- Suggestions where applicable

### Distribution
- Packaged as standalone Windows executable
- No Python installation required for end users

---

## Out of Scope — V3.0.0

These are explicitly excluded from V3.0.0.
They may be reconsidered in future versions.

- Match history or saved sessions
- Multiple game mode support
- Map-based analysis
- Weapon attachments
- Database or file storage
- Multiplayer or online features
- AI or machine learning predictions
- CLI interface
- Web interface
- Themes beyond the default dark theme
- Export to PDF or CSV

---

## Success Criteria

V3.0.0 is considered complete when:

- [ ] All five weapons are implemented and tested
- [ ] Validation handles all known edge cases from V2.9 test suite
- [ ] UI displays results as severity-colored cards
- [ ] Application never crashes on any user input
- [ ] All modules have unit tests
- [ ] All documentation is complete
- [ ] Executable is buildable via PyInstaller
- [ ] A GitHub release can be created confidently

---

## Constraints

- Python standard library only (no third-party packages except PyInstaller)
- Tkinter for UI (no PyQt, no Kivy)
- Must run on Windows without Python installed (via executable)
- Analysis logic must never live inside UI code
- No direct print statements outside of run.py startup logging

---

## Known Limitations Carried From V2.9

- Accuracy is used as a proxy for aim quality, not a direct measure
- K/D is used as a proxy for combat efficiency, not a direct measure
- Heuristics may produce false positives near threshold boundaries
- Small sample suppression threshold is heuristic, not mathematically proven
- Kill and death limits (200) are based on typical match expectations,
  not guaranteed across all game modes

---

## Version History Reference

| Version | Status |
|---------|--------|
| V1 - V2.9 | Legacy procedural script |
| V3.0.0 | Current development target |
| V3.1.0 | Future, not yet planned |

---

*This document defines what Playlytics V3 is and is not.*
*Any feature not listed here requires a PRD update before implementation.*