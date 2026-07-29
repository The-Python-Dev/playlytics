# Rules.md — Playlytics V3
# AI Collaboration Rules and Project Boundaries

---

## Purpose

This document defines the rules that govern how this project
is built and how the AI assistant collaborates on it.

It exists to prevent scope creep, maintain architectural integrity,
and ensure every decision is intentional.

---

## Core Development Rules

### Rule 1 — Architecture First
No code is written until the architecture is approved.
No architecture changes are made without updating ARCHITECTURE.md first.

### Rule 2 — One Module at a Time
Build one module completely before starting the next.
Complete means: coded, tested, reviewed, documented, committed.

### Rule 3 — No Skipping Steps
Every module goes through this sequence:
1. Purpose explained
2. Interface designed
3. Trade-offs discussed
4. Implementation written
5. Reviewed
6. Tested
7. Documentation updated
8. Git commit message provided

### Rule 4 — Tests Are Not Optional
Every module gets unit tests before the next module begins.
Tests are written alongside code, not after everything is built.

### Rule 5 — Documentation Is Not Optional
CHANGELOG.md, ARCHITECTURE.md, and Memory.md are updated
after every completed module.
Documentation is never left until the end.

### Rule 6 — No Feature Creep
If a feature is not listed in PRD.md it does not get built.
Any new feature requires a PRD.md update and explicit approval first.

### Rule 7 — YAGNI
Do not build what is not needed yet.
Do not add abstractions for hypothetical future requirements.
Build for V3.0.0. Think about V3.1.0 later.

### Rule 8 — Commit After Every Module
Every completed module gets a Git commit.
Commit messages follow the conventional commits format.

---

## AI Collaboration Rules

### AI Rule 1 — Never Generate the Entire Project at Once
Work iteratively, one module at a time.
Do not jump ahead without approval.

### AI Rule 2 — Challenge Poor Decisions
If a design decision is questionable, say so.
Explain why and suggest a better alternative.
Do not silently implement bad architecture to be agreeable.

### AI Rule 3 — Ask Before Assuming
If requirements are unclear, ask.
Do not invent features or behaviors that were not specified.

### AI Rule 4 — Respect Approved Decisions
Once a design decision is approved, implement it as approved.
Do not quietly change architecture mid-implementation.

### AI Rule 5 — Keep Memory.md Updated
After every module, Memory.md is updated with current progress.
This ensures context is preserved across sessions.

### AI Rule 6 — Flag Scope Creep Immediately
If a request would add something outside PRD.md, flag it.
Do not silently expand scope.

### AI Rule 7 — Never Sacrifice Maintainability for Convenience
If the easy solution creates technical debt, say so.
Recommend the maintainable solution even if it takes longer.

---

## Library Rules

### Allowed
- Python Standard Library (all modules)
- Tkinter (UI only)
- unittest (testing)
- logging (logging only)
- PyInstaller (packaging only, not imported in code)

### Not Allowed
- PyQt, Kivy, or any non-Tkinter UI framework
- Third-party analysis libraries
- Third-party testing frameworks (pytest is acceptable
  if explicitly approved)
- Any library that creates unnecessary external dependencies

### Rule
If a library is not in the allowed list above,
it requires explicit approval before use.

---

## Code Rules

### No Direct Printing
No module prints directly except run.py startup messages.
All output is returned as structured objects.

### No exit() Calls
exit() is never used for flow control.
Validation returns ValidationResult.
The UI decides what to do with errors.

### No Analysis in the UI
UI code collects input and displays output only.
Zero analysis logic lives in app.py, input_view.py,
or result_view.py.

### No Magic Numbers
All thresholds and limits live in core/config.py.
No hardcoded numeric values anywhere else.

### Logging Not Printing
Use logging.getLogger(__name__) in every module.
Never use print() for debugging or diagnostics.

### Type Hints Encouraged
Add type hints where they improve clarity.
Do not add type hints that make simple code harder to read.

### Docstrings Required
Every module, class, and public function gets a docstring.
Docstrings explain purpose, not implementation details.

---

## Error Handling Rules

### User Errors
- Caught by the validation layer
- Returned as ValidationResult with is_valid=False
- Displayed as ERROR severity cards in the UI
- Never crash the application

### Unexpected Errors
- Caught by the controller
- Logged using the logger
- Returned as ControllerResult with success=False
- Displayed as a generic friendly error message
- Never expose stack traces to the user

### Never
- Never let the application crash on user input
- Never show raw exception messages to the user
- Never use bare except clauses
- Never silence exceptions without logging them

---

## Architecture Rules

### Single Responsibility
Every module has exactly one reason to exist.
If a module is doing two things, split it.

### Dependency Direction
Dependencies flow downward only.

UI
↓
Controller
↓
Validation / Analyzer Engine
↓
Rules / Weapons
↓
Models
↓
Core

No lower layer imports from a higher layer.
Models never import from UI.
Rules never import from the controller.

### Immutability
Configuration is a frozen dataclass.
PlayerStats and Metrics are not mutated after creation.
Analysis never modifies its input data.

### Structured Results Only
Every layer returns a typed object.
No layer returns raw strings as its primary output.
No layer returns None when a result object is expected.

---

## What This Project Is Not

- Not a data science project
- Not a machine learning project
- Not a web application
- Not a multiplayer tool
- Not a database application
- Not a commercial product

It is a portfolio-quality desktop application that demonstrates
clean software engineering on a focused, well-understood problem.

---

## Violation Protocol

If any rule is violated during development:

1. Stop immediately
2. Identify which rule was violated
3. Understand why it was violated
4. Fix it before continuing
5. Update Memory.md to note what happened

Rules exist to protect the project from shortcuts that
create long-term problems.

---

*This document governs how Playlytics V3 is built.*
*It is not optional and not negotiable.*