# Memory.md — Playlytics V3
# AI Collaboration Memory File

---

## Purpose

This file exists to preserve context across chat sessions.

When a new session begins, this file is read first.
It tells the AI exactly where development is,
what decisions have been made, and what comes next.

Without this file, context is lost and work is repeated.
This file prevents that.

---

## How To Use This File

At the start of every new session:
1. Share this file with the AI
2. The AI reads it completely before responding
3. Development continues from exactly where it left off

After every completed module:
1. Update the Current Status section
2. Update the Completed Modules section
3. Update the Next Module section
4. Commit the updated Memory.md alongside the module

---

## Project Identity

| Property        | Value                                      |
|-----------------|--------------------------------------------|
| Project Name    | Playlytics V3                              |
| Version Target  | 3.0.0                                      |
| Type            | Desktop Application                        |
| Language        | Python 3                                   |
| UI Framework    | Tkinter                                    |
| Packaging       | PyInstaller                                |
| License         | MIT                                        |
| Repository      | [Add GitHub URL when created]              |

---

## Current Status

**Phase:** 1 — Models
**Current Module:** models/validation_result.py
**Overall Progress:** 5 of 28 modules complete

Last action completed:
- models/analysis_result.py implemented and tested (6 tests passing)
- CHANGELOG.md updated

Next action:
- Implement models/validation_result.py

## Approved Architecture

Architecture is fully approved and locked.
Do not redesign unless a genuine flaw is discovered.
Full details in docs/ARCHITECTURE.md.

### Data Flow
```
User Input (raw strings)
        ↓
ui/app.py
        ↓
ui/controller.py
        ↓
validation/validator.py → ValidationResult
        ↓
analyzers/metrics_calculator.py → Metrics
        ↓
rules/engine.py → list of RuleResult
        ↓
analyzers/router.py → weapon analyzer
        ↓
analyzers/weapons/<weapon>.py → list of RuleResult
        ↓
analyzers/engine.py → AnalysisResult
        ↓
ui/controller.py → ControllerResult
        ↓
ui/views/result_view.py

---

## Implementation Order

Phase 1 — Models
✅ models/severity.py
✅ models/rule_result.py
✅ models/player_stats.py
✅ models/metrics.py
✅ models/analysis_result.py
⏳ models/validation_result.py    ← CURRENT
⬜ models/controller_result.py
⬜ models/configuration.py

Phase 2 — Core
⬜ core/config.py
⬜ core/exceptions.py
⬜ core/logger.py

Phase 3 — Validation
⬜ validation/normalizer.py
⬜ validation/boundaries.py
⬜ validation/validator.py

Phase 4 — Metrics Calculator
⬜ analyzers/metrics_calculator.py

Phase 5 — Rule Engine
⬜ rules/base.py
⬜ rules/context.py
⬜ rules/rules/accuracy_rule.py
⬜ rules/rules/kd_rule.py
⬜ rules/rules/positioning_rule.py
⬜ rules/rules/survival_rule.py
⬜ rules/rules/small_sample_rule.py
⬜ rules/engine.py

Phase 6 — Weapon Analyzers
⬜ analyzers/weapons/base.py
⬜ analyzers/weapons/sniper.py
⬜ analyzers/weapons/smg.py
⬜ analyzers/weapons/assault.py
⬜ analyzers/weapons/lmg.py
⬜ analyzers/weapons/shotgun.py

Phase 7 — Router and Engine
⬜ analyzers/router.py
⬜ analyzers/engine.py

Phase 8 — Controller
⬜ ui/controller.py

Phase 9 — UI
⬜ utils/formatters.py
⬜ ui/views/input_view.py
⬜ ui/views/result_view.py
⬜ ui/app.py

Phase 10 — Integration
⬜ run.py

Phase 11 — Packaging and Release
⬜ PyInstaller spec
⬜ Executable build
⬜ GitHub release

---

## Completed Modules

### models/severity.py
**Status:** ✅ Complete
**Tests:** 5 passing (pytest)
**Location:** src/models/severity.py
**Test Location:** tests/test_models/test_severity.py
**Description:**
Severity enum with four levels: SUCCESS, INFO, WARNING, ERROR.
Used by all result types to communicate meaning to the UI layer
without string matching.
**Commit:** feat(models): add Severity enum with tests

### models/rule_result.py
**Status:** ✅ Complete
**Tests:** 6 passing (pytest)
**Location:** src/models/rule_result.py
**Test Location:** tests/test_models/test_rule_result.py
**Description:**
RuleResult dataclass representing the output of a single rule evaluation.
Holds rule_name, severity, message, optional suggestion, and passed flag.
Produced by every rule, consumed by the UI renderer.
**Commit:** feat(models): add RuleResult dataclass with tests

### models/player_stats.py
**Status:** ✅ Complete
**Tests:** 7 passing (pytest)
**Location:** src/models/player_stats.py
**Test Location:** tests/test_models/test_player_stats.py
**Description:**
Frozen dataclass holding validated raw player input.
Kills, deaths, accuracy, and weapon.
Immutable to prevent accidental mutation during analysis.
Derived values (K/D) live separately in Metrics.
**Commit:** feat(models): add PlayerStats frozen dataclass with tests

### models/metrics.py
**Status:** ✅ Complete
**Tests:** 7 passing (pytest)
**Location:** src/models/metrics.py
**Test Location:** tests/test_models/test_metrics.py
**Description:**
Frozen dataclass holding computed values derived from PlayerStats.
K/D ratio, sample size, and small sample flag.
Produced by MetricsCalculator, consumed by rules and analyzers.
**Commit:** feat(models): add Metrics frozen dataclass with tests

### models/analysis_result.py
**Status:** ✅ Complete
**Tests:** 6 passing (pytest)
**Location:** src/models/analysis_result.py
**Test Location:** tests/test_models/test_analysis_result.py
**Description:**
Frozen dataclass bundling the complete output of the analysis pipeline.
Holds original stats, computed metrics, all rule results as a flat list,
and a one-line summary. Consumed by the UI renderer.
**Commit:** feat(models): add AnalysisResult frozen dataclass with tests

## Key Design Decisions (Locked)

| Decision | Choice | Reason |
|----------|--------|--------|
| Output format | Structured objects only | Decouples analysis from display |
| Validation failure | Return ValidationResult | Never use exit() |
| Small sample suppression | Handled in analyzer engine | Not duplicated in each weapon |
| Unknown weapon | Return ERROR RuleResult | No crash, no exit() |
| Configuration | Frozen dataclass | Prevent mutation during analysis |
| Severity | Enum not strings | Type safe, typo proof |
| Printing | Never outside run.py | Keeps analysis testable |
| KD calculation | kills / deaths, deaths=0 returns kills | Matches V2.9 behavior |
| Sample size threshold | kills + deaths < 5 | Matches V2.9 behavior |
| Kill / death limit | 0 to 200 inclusive | Matches V2.9 behavior |
| Accuracy limit | 0.0 to 100.0 inclusive | Matches V2.9 behavior |

---

## Thresholds (From V2.9, Locked Until Config Phase)

| Constant | Value | Meaning |
|----------|-------|---------|
| HIGH_ACCURACY | 50 | Threshold for high accuracy |
| MID_ACCURACY | 40 | Threshold for mid accuracy |
| LOW_ACCURACY | 20 | Threshold for low accuracy |
| STRONG_KD | 2 | Threshold for strong K/D |
| WEAK_KD | 1 | Threshold for weak K/D |
| MIN_SAMPLE_SIZE | 5 | Minimum kills+deaths for analysis |
| MAX_KILLS | 200 | Upper bound for kills |
| MAX_DEATHS | 200 | Upper bound for deaths |

---

## Supported Weapons

| Input Accepted | Canonical Name |
|----------------|----------------|
| sniper | sniper |
| smg | smg |
| ar | assault |
| assault | assault |
| lmg | lmg |
| shotgun | shotgun |

---

## V2.9 Regression Cases (Must All Pass in V3)

These are the cases from TEST_CASES.md that V3 must not break.

| Case | Input | Expected |
|------|-------|----------|
| B1 | 4/0/20/ar | Perfect survival, no crash |
| B2 | 2/1/30/ar | Small sample message |
| B3 | 4/1/90/sniper | Sniper specialist triggers |
| B4 | 200/10/50/ar | Valid, analysis runs |
| B5 | 201/10/50/ar | Validation stops analysis |
| C1 | 5/10/60/ar | Positioning weak, survival issue |
| C2 | 10/4/37/lmg | Anchor play, no overlap |
| N1 | -3/4/70/smg | Validation stops analysis |
| N2 | 5/4/140/sniper | Validation stops analysis |
| N3 | "AR " | Normalized and accepted |
| N4 | 10000/3000/70/sniper | Validation stops analysis |
| F1 | 1/0/95/sniper | No sniper specialist (small sample) |
| F2 | 10/5/30/lmg | No camper conflict |
| F3 | 2/1/90/sniper | No sniper specialist (small sample) |
| P1 | 8/4/39/ar | Passive tendency near threshold |
| P2 | 2/0/95/sniper | Small sample suppression active |
| P3-A | 5/5/20/ar | Average aim triggers |
| P3-B | 5/4/40/ar | Strong performance triggers |
| P3-C | 6/2/50/sniper | Sniper boundary check |
| P4 | various | Normalization works |
| M1 | 15/5/70/ar | AR rusher detected |
| M2 | 10/4/37/lmg | Anchor play triggers |
| M3 | 2/1/37/lmg | Small sample suppresses LMG |
| M4 | 10/5/50/ar | AR rusher boundary respected |
| M5 | 7/10/55/shotgun | Shotgun warning triggers |
| M6 | 4/1/90/sniper | Sniper specialist at boundary |

---

## Rules That Govern This Project

1. One module at a time
2. Every module tested before moving on
3. No feature creep
4. No exit() calls
5. No printing outside run.py
6. No analysis in UI code
7. No magic numbers outside config.py
8. Architecture changes require ARCHITECTURE.md update first
9. Memory.md updated after every module
10. Commit after every completed module

Full rules in docs/Rules.md

---

## Known Issues Carried From V2.9

- Accuracy boundary at exactly 40 and 50 has
  partial pass behavior (> vs >= question)
- Camper heuristic may still be broad near thresholds
- Small sample threshold is heuristic, not mathematically proven

These are documented in docs/KNOWN_ISSUES.md

---

## Documents Created

| Document | Status |
|----------|--------|
| docs/PRD.md | ✅ Complete |
| docs/ARCHITECTURE.md | ✅ Complete |
| docs/Rules.md | ✅ Complete |
| docs/Phases.md | ✅ Complete |
| docs/Design.md | ✅ Complete |
| docs/Memory.md | ✅ Complete |
| CHANGELOG.md | ✅ Complete |
| docs/ROADMAP.md | ⬜ Not yet written |
| docs/TEST_CASES.md | ⬜ To be migrated from V2.9 |
| docs/KNOWN_ISSUES.md | ⬜ Not yet written |
| README.md | ⬜ Not yet written |

---

## Session Notes

### Session 1
- Read all V2.9 source material
- Designed and approved full architecture
- Completed models/severity.py
- Created all six planning documents

### Session 2
- Reorganized folder structure (app/ → src/)
- Created full layered folder structure
- Deleted old prototype code
- Set up git repository
- Adopted pytest for testing
- Completed models/severity.py with tests
- Updated CHANGELOG.md and Memory.md
---

*This file is the memory of Playlytics V3.*
*Read it at the start of every session.*
*Update it at the end of every module.*
*Never let it go stale.*