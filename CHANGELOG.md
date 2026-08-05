# Changelog

All notable changes to Playlytics V3 are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased] — 3.0.0 In Development

### Added
- Full project structure created (src/, tests/, docs/)
- Planning documentation (PRD, Architecture, Rules, Phases, Design, Memory)
- models/severity.py: Severity enum with four levels
  (SUCCESS, INFO, WARNING, ERROR)
- Unit tests for Severity enum (5 tests, all passing)
- models/rule_result.py: RuleResult dataclass for single rule evaluation output
- Unit tests for RuleResult (6 tests, all passing)
- models/player_stats.py: PlayerStats frozen dataclass for validated raw input
- Unit tests for PlayerStats (7 tests, all passing)
- models/metrics.py: Metrics frozen dataclass for computed values
- Unit tests for Metrics (7 tests, all passing)

### Infrastructure
- Git repository initialized
- .gitignore configured
- pytest adopted as testing framework