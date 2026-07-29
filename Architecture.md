# ARCHITECTURE.md — Playlytics V3
# Architecture Document

---

## Overview

Playlytics V3 is a modular desktop application built with Python 3 and Tkinter.

The architecture is designed around a single principle:

> Every layer has one responsibility and one responsibility only.

UI collects input and displays output.
Analysis logic never touches the UI.
Validation runs before analysis.
Results are structured objects, never raw strings.

---

## Technology Stack

| Component        | Technology              |
|------------------|-------------------------|
| Language         | Python 3                |
| UI Framework     | Tkinter                 |
| Packaging        | PyInstaller             |
| Dependencies     | Python Standard Library |
| Testing          | unittest                |
| Version Control  | Git / GitHub            |

---

## Folder Structure

```
playlytics/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── VERSION
├── requirements.txt
├── run.py
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── ROADMAP.md
│   ├── TEST_CASES.md
│   ├── KNOWN_ISSUES.md
│   ├── Rules.md
│   ├── Phases.md
│   ├── Design.md
│   └── Memory.md
│
├── src/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── logger.py
│   │
│   ├── models/
│   │   ├── configuration.py
│   │   ├── player_stats.py
│   │   ├── metrics.py
│   │   ├── analysis_result.py
│   │   ├── rule_result.py
│   │   ├── validation_result.py
│   │   ├── controller_result.py
│   │   └── severity.py
│   │
│   ├── validation/
│   │   ├── validator.py
│   │   ├── boundaries.py
│   │   └── normalizer.py
│   │
│   ├── analyzers/
│   │   ├── engine.py
│   │   ├── router.py
│   │   ├── metrics_calculator.py
│   │   └── weapons/
│   │       ├── base.py
│   │       ├── sniper.py
│   │       ├── smg.py
│   │       ├── assault.py
│   │       ├── lmg.py
│   │       └── shotgun.py
│   │
│   ├── rules/
│   │   ├── engine.py
│   │   ├── base.py
│   │   ├── context.py
│   │   └── rules/
│   │       ├── accuracy_rule.py
│   │       ├── kd_rule.py
│   │       ├── positioning_rule.py
│   │       ├── survival_rule.py
│   │       └── small_sample_rule.py
│   │
│   ├── ui/
│   │   ├── app.py
│   │   ├── controller.py
│   │   └── views/
│   │       ├── input_view.py
│   │       └── result_view.py
│   │
│   ├── utils/
│   │   └── formatters.py
│   │
│   └── assets/
│
└── tests/
    ├── conftest.py
    ├── test_validation.py
    ├── test_analyzer_engine.py
    ├── test_weapon_router.py
    ├── test_metrics_calculator.py
    ├── test_models/
    ├── test_rules/
    ├── test_weapons/
    └── test_ui/
```

---

## Data Flow

```
User Input (raw strings)
        ↓
ui/app.py
Collects input from UI fields
        ↓
ui/controller.py
Coordinates the full pipeline
        ↓
validation/validator.py
Parses, normalizes, validates
Returns ValidationResult
        ↓
analyzers/metrics_calculator.py
Computes K/D, sample size, small sample flag
Returns Metrics object
        ↓
rules/engine.py
Evaluates general performance rules
Returns list of RuleResult objects
        ↓
analyzers/router.py
Selects correct weapon analyzer
        ↓
analyzers/weapons/<weapon>.py
Evaluates weapon-specific rules
Returns list of RuleResult objects
        ↓
analyzers/engine.py
Combines all RuleResults into AnalysisResult
        ↓
ui/controller.py
Wraps AnalysisResult in ControllerResult
        ↓
ui/views/result_view.py
Renders result cards to the screen
```

---

## Layer Responsibilities

### run.py
- Entry point only
- Starts the application
- Contains zero logic

---

### ui/app.py
- Builds the Tkinter window
- Manages layout
- Delegates to input_view and result_view

---

### ui/controller.py
- Coordinates the full analysis pipeline
- Calls validation, analyzer engine
- Returns ControllerResult
- Catches unexpected exceptions
- Never performs analysis itself

---

### ui/views/input_view.py
- Renders the input form
- Collects raw user input
- Passes raw strings to controller
- No validation or analysis logic

---

### ui/views/result_view.py
- Receives AnalysisResult
- Renders result cards
- Card color determined by Severity
- No analysis logic

---

### validation/normalizer.py
- Strips whitespace
- Converts to lowercase
- Resolves aliases (ar → assault)

---

### validation/boundaries.py
- Defines valid ranges
- Checks kills, deaths, accuracy limits
- Checks supported weapon list

---

### validation/validator.py
- Orchestrates normalization and boundary checks
- Returns ValidationResult
- Never raises exceptions to caller

---

### core/config.py
- Central constants file
- Thresholds, limits, supported weapons
- Single source of truth for all magic numbers

---

### models/configuration.py
- Immutable frozen dataclass
- Wraps config values into a typed object
- Passed into analyzers and rules

---

### models/player_stats.py
- Simple data container
- Holds raw validated input: kills, deaths, accuracy, gun

---

### models/metrics.py
- Holds computed values: kd_ratio, sample_size, is_small_sample
- Produced by MetricsCalculator

---

### models/severity.py
- Enum: SUCCESS, INFO, WARNING, ERROR
- Used by all result types

---

### models/rule_result.py
- Output of one rule evaluation
- Holds: rule_name, passed, severity, message, suggestion

---

### models/analysis_result.py
- Complete output of the analysis pipeline
- Holds: weapon, stats, metrics, rule_results, summary

---

### models/validation_result.py
- Output of the validation layer
- Holds: is_valid, data, errors

---

### models/controller_result.py
- Output of the controller
- Holds: success, result, errors
- One predictable return type for the UI

---

### analyzers/metrics_calculator.py
- Computes K/D ratio
- Computes sample size
- Sets small sample flag
- Returns Metrics object

---

### rules/base.py
- Abstract base class for all rules
- Defines the evaluate() interface

---

### rules/context.py
- Data container passed into every rule
- Holds: stats, metrics, configuration

---

### rules/engine.py
- Runs all general rules against the context
- Returns list of RuleResult objects

---

### rules/rules/
- One file per rule
- accuracy_rule.py
- kd_rule.py
- positioning_rule.py
- survival_rule.py
- small_sample_rule.py

---

### analyzers/weapons/base.py
- Abstract base class for all weapon analyzers
- Defines the analyze() interface

---

### analyzers/weapons/
- One file per weapon
- Each receives PlayerStats and Metrics
- Each returns list of RuleResult objects
- No printing, no side effects

---

### analyzers/router.py
- Maps weapon name to correct analyzer
- Returns structured error if weapon unknown

---

### analyzers/engine.py
- Orchestrates MetricsCalculator, RuleEngine, Router
- Combines all results into AnalysisResult
- Suppresses weapon analysis if small sample detected

---

### utils/formatters.py
- String formatting helpers
- Used by result_view for display formatting

---

### core/exceptions.py
- Custom exception classes
- Used internally, never exposed to the user directly

---

### core/logger.py
- Configures application-wide logging
- Every module uses logging.getLogger(__name__)

---

## Key Design Decisions

### Decision 1 — No direct printing anywhere except run.py startup
Every module returns structured objects.
Analysis is fully decoupled from output.

### Decision 2 — Validation returns ValidationResult, never raises
The UI handles errors gracefully.
No exit() calls anywhere in the application.

### Decision 3 — Small sample suppression lives in the analyzer engine
The engine decides whether to call weapon analyzers.
Weapon files do not handle sample size themselves.

### Decision 4 — Router returns structured error on unknown weapon
Unknown gun type produces a RuleResult with ERROR severity.
The UI displays it like any other result.

### Decision 5 — Match object replaced by PlayerStats + Metrics
Separating raw input from computed values keeps responsibilities clean.
PlayerStats holds what the user entered.
Metrics holds what the system calculated.

### Decision 6 — Configuration is immutable
Frozen dataclass prevents accidental mutation of thresholds
during analysis.

---

## Supported Weapons — V3.0.0

| Input | Canonical Name |
|-------|---------------|
| sniper | sniper |
| smg | smg |
| ar | assault |
| assault | assault |
| lmg | lmg |
| shotgun | shotgun |

---

## Testing Strategy

Every module has a corresponding test file.
Tests are written alongside each module, not after.
V2.9 regression cases are migrated into the test suite.

| Test File | Covers |
|-----------|--------|
| test_validation.py | Normalizer, boundaries, validator |
| test_analyzer_engine.py | Engine orchestration |
| test_weapon_router.py | Routing logic |
| test_metrics_calculator.py | K/D, sample size |
| test_models/ | All model classes |
| test_rules/ | Each rule in isolation |
| test_weapons/ | Each weapon analyzer |
| test_ui/ | Controller result handling |

---

## Versioning

Semantic Versioning is used.

MAJOR.MINOR.PATCH

| Change Type | Version Bump |
|-------------|-------------|
| Breaking changes | MAJOR |
| New features | MINOR |
| Bug fixes | PATCH |

Current target: v3.0.0

---

*This document is the single source of truth for V3 architecture.*
*Any structural change requires this document to be updated first.*