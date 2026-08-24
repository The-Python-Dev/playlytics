# Phases.md — Playlytics V3
# Development Phases

---

## Purpose

This document breaks the V3.0.0 development into manageable,
sequential phases.

Each phase has a clear goal, a defined set of deliverables,
and a completion criteria.

No phase begins until the previous phase is complete.

---

## Implementation Rules

- One module at a time within each phase
- Every module is coded, tested, reviewed, and committed
  before the next module begins
- Memory.md is updated after every completed module
- CHANGELOG.md is updated after every completed phase
- No phase is marked complete until all deliverables are done

---

## Phase 0 — Project Setup

### Goal
Establish the project foundation before any code is written.

### Deliverables
- [ ] Repository created on GitHub
- [ ] Folder structure created
- [ ] README.md written
- [ ] CHANGELOG.md initialized
- [ ] LICENSE added (MIT)
- [ ] VERSION file created (3.0.0)
- [ ] requirements.txt created
- [ ] All docs/ files created:
      PRD.md
      ARCHITECTURE.md
      Rules.md
      Phases.md
      Design.md
      Memory.md
      ROADMAP.md
      TEST_CASES.md
      KNOWN_ISSUES.md
- [ ] run.py stub created
- [ ] .gitignore created

### Completion Criteria
Repository is clean, documented, and ready for development.
Another developer could read the docs and understand
what is being built before a single line of logic exists.

### Git Commit
docs: initialize project structure and documentation

---

## Phase 1 — Models

### Goal
Build all data models that every other layer depends on.
No logic. No analysis. Pure data containers and enums.

### Deliverables
- [ ] models/severity.py
- [ ] models/rule_result.py
- [ ] models/analysis_result.py
- [ ] models/validation_result.py
- [ ] models/controller_result.py
- [ ] models/player_stats.py
- [ ] models/metrics.py
- [ ] models/configuration.py
- [ ] tests/test_models/ for each model

### Completion Criteria
All models exist, are tested, and are importable.
No other layer has been touched.

### Git Commit Per Module
feat(models): add <module name>

---

## Phase 2 — Core

### Goal
Build the foundational utilities that support all other layers.

### Deliverables
- [ ] core/config.py
- [ ] core/exceptions.py
- [ ] core/logger.py

### Completion Criteria
Constants are centralized.
Custom exceptions exist.
Logging is configured.
All modules tested.

### Git Commit Per Module
feat(core): add <module name>

---

## Phase 3 — Validation

### Goal
Build the validation layer that protects the analyzer
from invalid input.

### Deliverables
- [ ] validation/normalizer.py
- [ ] validation/boundaries.py
- [ ] validation/validator.py
- [ ] tests/test_validation.py

### Completion Criteria
All V2.9 validation test cases pass.
Invalid input never reaches the analyzer.
No exit() calls.
No exceptions raised to the caller.
ValidationResult returned in all cases.

### Key Test Cases To Pass
- Negative kills rejected
- Negative deaths rejected
- Accuracy above 100 rejected
- Accuracy below 0 rejected
- Kills above 200 rejected
- Deaths above 200 rejected
- Unknown gun type rejected
- Non-numeric input rejected
- Whitespace stripped correctly
- Aliases resolved correctly (ar → assault)
- Empty input rejected

### Git Commit Per Module
feat(validation): add <module name>

---

## Phase 4 — Metrics Calculator

### Goal
Build the component that computes derived metrics
from validated player stats.

### Deliverables
- [ ] analyzers/metrics_calculator.py
- [ ] tests/test_metrics_calculator.py

### Completion Criteria
K/D ratio computed correctly.
Zero death case handled without division error.
Sample size computed correctly.
Small sample flag set correctly at boundary (kills + deaths < 5).
Metrics object returned.

### Key Test Cases To Pass
- Deaths = 0 returns kills as K/D
- Kills = 0 returns 0.0 as K/D
- Sample size below threshold sets is_small_sample = True
- Sample size at threshold sets is_small_sample = False
- K/D rounded to 2 decimal places

### Git Commit
feat(analyzers): add metrics_calculator

---

## Phase 5 — Rule Engine

### Goal
Build the general rule evaluation system.
Each rule is its own class.
No giant if/elif chains.

### Deliverables
- [ ] rules/base.py
- [ ] rules/context.py
- [ ] rules/rules/accuracy_rule.py
- [ ] rules/rules/kd_rule.py
- [ ] rules/rules/positioning_rule.py
- [ ] rules/rules/survival_rule.py
- [ ] rules/rules/small_sample_rule.py
- [ ] rules/engine.py
- [ ] tests/test_rules/ for each rule

### Completion Criteria
Each rule evaluated independently.
Each rule returns a RuleResult.
Rules do not depend on each other.
Rule engine runs all rules and returns a list of RuleResults.
All V2.9 general analysis cases produce correct results.

### Git Commit Per Module
feat(rules): add <module name>

---

## Phase 6 — Weapon Analyzers

### Goal
Build all five weapon-specific analyzers.
Each analyzer is isolated and independently testable.

### Deliverables
- [ ] analyzers/weapons/base.py
- [ ] analyzers/weapons/sniper.py
- [ ] analyzers/weapons/smg.py
- [ ] analyzers/weapons/assault.py
- [ ] analyzers/weapons/lmg.py
- [ ] analyzers/weapons/shotgun.py
- [ ] tests/test_weapons/ for each weapon

### Completion Criteria
Each weapon analyzer tested in isolation.
Each weapon returns correct RuleResults for all V2.9 cases.
No weapon analyzer handles small sample suppression itself.
No weapon analyzer prints anything.

### Key Test Cases To Pass
- Sniper specialist triggers correctly
- Sniper specialist does not trigger on small sample
- SMG over-aggression triggers correctly
- LMG anchor play triggers correctly
- LMG overlap with passive heuristic resolved
- AR rusher triggers correctly
- Shotgun warning triggers correctly

### Git Commit Per Weapon
feat(weapons): add <weapon name> analyzer

---

## Phase 7 — Router and Analyzer Engine

### Goal
Connect all analyzers through the router.
Build the engine that orchestrates the full analysis pipeline.

### Deliverables
- [ ] analyzers/router.py
- [ ] analyzers/engine.py
- [ ] tests/test_weapon_router.py
- [ ] tests/test_analyzer_engine.py

### Completion Criteria
Router maps all supported weapons correctly.
Router returns structured error for unknown weapon.
Engine suppresses weapon analysis on small sample.
Engine combines general and weapon results into AnalysisResult.
Full pipeline produces correct output for all V2.9 test cases.

### Git Commit Per Module
feat(analyzers): add <module name>

---

## Phase 8 — Controller

### Goal
Build the controller that coordinates the full pipeline
and provides one predictable result type to the UI.

### Deliverables
- [ ] ui/controller.py
- [ ] tests/test_ui/ controller tests

### Completion Criteria
Controller calls validation, then analyzer engine.
Controller returns ControllerResult in all cases.
Controller catches unexpected exceptions and logs them.
Controller never crashes.
Controller never performs analysis itself.

### Git Commit
feat(ui): add controller

---

## Phase 9 — UI

### Goal
Build the Tkinter interface that collects input
and displays results.

### Deliverables
- [ ] ui/views/input_view.py
- [ ] ui/views/result_view.py
- [ ] ui/app.py
- [ ] utils/formatters.py

### Completion Criteria
Input form collects all required fields.
Results displayed as severity-colored cards.
No analysis logic in any UI file.
Application handles all error states gracefully.
UI never crashes on any input.

### Git Commit Per Module
feat(ui): add <module name>

---

## Phase 10 — Entry Point and Integration

### Goal
Wire everything together and verify the full application works
end to end.

### Deliverables
- [ ] run.py completed
- [ ] Full end-to-end manual test against all V2.9 test cases
- [ ] All automated tests passing
- [ ] No known crashes

### Completion Criteria
Application launches from run.py
All test cases from TEST_CASES.md produce correct results.
No regressions from V2.9 behavior.

### Git Commit
feat: complete run.py and full integration

---

## Phase 11 — Packaging and Release

### Goal
Package the application as a standalone executable
and prepare a GitHub release.

### Deliverables
- [ ] PyInstaller spec file created
- [ ] Executable built and tested on Windows
- [ ] README.md completed with screenshots
- [ ] CHANGELOG.md finalized for v3.0.0
- [ ] KNOWN_ISSUES.md updated
- [ ] GitHub release created with executable attached
- [ ] Version tag v3.0.0 pushed to repository

### Completion Criteria
Executable runs on a machine without Python installed.
GitHub release is clean, professional, and complete.
Repository is ready to be shared as a portfolio project.

### Git Commit
release: v3.0.0

---

### Phase Summary

| Phase | Name | Status |
|-------|------|--------|
| 0 | Project Setup | ✅ Complete |
| 1 | Models | ✅ Complete |
| 2 | Core | ✅ Complete |
| 3 | Validation | ✅ Complete |
| 4 | Metrics Calculator | ✅ Complete |
| 5 | Rule Engine | ⏳ Starting |
| 6 | Weapon Analyzers | ⬜ Not Started |
| 7 | Router and Engine | ⬜ Not Started |
| 8 | Controller | ⬜ Not Started |
| 9 | UI | ⬜ Not Started |
| 10 | Integration | ⬜ Not Started |
| 11 | Packaging and Release | ⬜ Not Started |s

---

*This document is the development roadmap for Playlytics V3.0.0.*
*No phase is skipped. No phase is marked complete prematurely.*