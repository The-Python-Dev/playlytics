# Changelog

All notable changes to Playlytics V3 are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project follows [Semantic Versioning](https://semver.org/).

---

### Phase 1 Complete
- All 8 model classes implemented and tested (52 tests passing)
- Foundation layer ready for validation, rules, and analyzers

### Phase 2 Complete
- All 3 core utilities implemented and tested (30 tests passing)
- Foundation utilities ready for validation and analysis layers

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
- models/analysis_result.py: AnalysisResult frozen dataclass for full pipeline output
- Unit tests for AnalysisResult (6 tests, all passing)
- models/validation_result.py: ValidationResult frozen dataclass for validation output
- Unit tests for ValidationResult (7 tests, all passing)
- models/controller_result.py: ControllerResult frozen dataclass for pipeline output
- Unit tests for ControllerResult (7 tests, all passing)
- models/configuration.py: Configuration frozen dataclass for analyzer settings
- Unit tests for Configuration (7 tests, all passing)
- core/config.py: Single source of truth for all analyzer constants
- Unit tests for core/config (10 tests, all passing)
- core/exceptions.py: Custom exception hierarchy for internal errors
- Unit tests for core/exceptions (10 tests, all passing)
- core/logger.py: Application-wide logging configuration
- Unit tests for core/logger (10 tests, all passing)
- validation/normalizer.py: Input normalization (whitespace, casing, aliases)
- Unit tests for normalizer (20 tests, all passing)
- validation/boundaries.py: Range and type checks for normalized input
- Unit tests for boundaries (39 tests, all passing, includes V2.9 regression cases)

### Infrastructure
- Git repository initialized
- .gitignore configured
- pytest adopted as testing framework