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

**Phase:** 4 — Metrics Calculator (starting)
**Current Module:** analyzers/metrics_calculator.py
**Overall Progress:** 14 of 28 modules complete
**Total Tests:** ~154 passing
**Phase 3 Status:** ✅ COMPLETE

Last action completed:
- validation/validator.py implemented and tested (13 tests passing)
- Phase 3 (Validation) officially complete

Next action:
- Begin Phase 4 (Metrics Calculator)
- Implement analyzers/metrics_calculator.py

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

Phase 1 — Models ✅ COMPLETE
✅ models/severity.py
✅ models/rule_result.py
✅ models/player_stats.py
✅ models/metrics.py
✅ models/analysis_result.py
✅ models/validation_result.py
✅ models/controller_result.py
✅ models/configuration.py

Phase 2 — Core ✅ COMPLETE
✅ core/config.py
✅ core/exceptions.py
✅ core/logger.py

Phase 3 — Validation ✅ COMPLETE
✅ validation/normalizer.py
✅ validation/boundaries.py
✅ validation/validator.py

Phase 4 — Metrics Calculator
⏳ analyzers/metrics_calculator.py   ← CURRENTss

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

### models/validation_result.py
**Status:** ✅ Complete
**Tests:** 7 passing (pytest)
**Location:** src/models/validation_result.py
**Test Location:** tests/test_models/test_validation_result.py
**Description:**
Frozen dataclass for the output of the validation layer.
Holds is_valid flag, optional clean PlayerStats data, and a list
of human-readable error messages. Replaces the V2.9 exit() pattern
with structured, non-crashing error reporting.
**Commit:** feat(models): add ValidationResult frozen dataclass with tests

### models/controller_result.py
**Status:** ✅ Complete
**Tests:** 7 passing (pytest)
**Location:** src/models/controller_result.py
**Test Location:** tests/test_models/test_controller_result.py
**Description:**
Frozen dataclass representing the single predictable return type
from the controller to the UI. Wraps AnalysisResult on success,
or a list of error messages on failure. Ensures the UI never sees
raw exceptions or intermediate pipeline state.
**Commit:** feat(models): add ControllerResult frozen dataclass with tests

### models/configuration.py
**Status:** ✅ Complete
**Tests:** 7 passing (pytest)
**Location:** src/models/configuration.py
**Test Location:** tests/test_models/test_configuration.py
**Description:**
Frozen dataclass defining the shape of analyzer configuration.
Holds accuracy thresholds, K/D thresholds, sample size minimum,
input limits, and supported weapons tuple. Actual values live in
core/config.py. Passed as a dependency into rules and analyzers.
**Commit:** feat(models): add Configuration frozen dataclass with tests

### core/config.py
**Status:** ✅ Complete
**Tests:** 10 passing (pytest)
**Location:** src/core/config.py
**Test Location:** tests/test_core/test_config.py
**Description:**
Single source of truth for all analyzer constants. Holds accuracy
thresholds, K/D thresholds, sample size minimum, input limits,
supported weapons tuple, and weapon aliases. Provides
get_default_configuration() factory that builds the Configuration
object used throughout the analyzer. All values match V2.9 exactly.
**Commit:** feat(core): add config module with constants and factory

### core/exceptions.py
**Status:** ✅ Complete
**Tests:** 10 passing (pytest)
**Location:** src/core/exceptions.py
**Test Location:** tests/test_core/test_exceptions.py
**Description:**
Custom exception hierarchy for internal analyzer errors.
Base class PlaylyticsError with three subclasses: ValidationError,
AnalysisError, and WeaponNotSupportedError. Never shown to the user.
Caught at the controller boundary and translated to safe messages.
**Commit:** feat(core): add custom exception hierarchy

### core/logger.py
**Status:** ✅ Complete
**Tests:** 10 passing (pytest)
**Location:** src/core/logger.py
**Test Location:** tests/test_core/test_logger.py
**Description:**
Application-wide logging configuration. Provides configure_logging()
for one-time setup at startup and get_logger() convenience wrapper.
Supports console output by default and optional file logging.
Uses standard library logging module only.
**Commit:** feat(core): add application logging configuration

### validation/normalizer.py
**Status:** ✅ Complete
**Tests:** 20 passing (pytest)
**Location:** src/validation/normalizer.py
**Test Location:** tests/test_validation/test_normalizer.py
**Description:**
First stage of the validation layer. Cleans raw user input:
strips whitespace, lowercases weapon strings, and resolves
known aliases (e.g. 'ar' -> 'assault'). Never fails.
Unknown inputs pass through unchanged for boundaries to reject.
**Commit:** feat(validation): add input normalizer

### validation/boundaries.py
**Status:** ✅ Complete
**Tests:** 39 passing (pytest)
**Location:** src/validation/boundaries.py
**Test Location:** tests/test_validation/test_boundaries.py
**Description:**
Second stage of the validation layer. Parses normalized string
input into numbers and verifies ranges. Individual check functions
per field (check_kills, check_deaths, check_accuracy, check_weapon)
plus a check_all combiner that collects all errors at once.
Never raises exceptions. Includes V2.9 regression tests.
**Commit:** feat(validation): add boundary checks with V2.9 regression tests

### validation/validator.py
**Status:** ✅ Complete
**Tests:** 13 passing (pytest)
**Location:** src/validation/validator.py
**Test Location:** tests/test_validation/test_validator.py
**Description:**
Main entry point for the validation layer. Orchestrates normalizer
and boundaries. Takes raw string input, returns ValidationResult
with either a clean PlayerStats or a list of human-readable errors.
Never raises exceptions. Never calls exit(). Includes V2.9 cases.
**Commit:** feat(validation): add validator orchestrator

## Phase Completion Log

### Phase 1 — Models ✅
**Completed:** [Add date]
**Modules:** 8
**Tests:** 52 passing
**Summary:**
All data models implemented and tested. Foundation layer complete.
Every subsequent phase can now depend on these typed, immutable objects.

### Phase 2 — Core ✅
**Completed:** [Add date]
**Modules:** 3
**Tests:** 30 passing
**Summary:**
Core utilities complete. Constants centralized, custom exceptions
defined, logging configured. Validation and analyzer layers can
now depend on this foundation.

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