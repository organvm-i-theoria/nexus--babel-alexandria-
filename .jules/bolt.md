## 2024-05-23 - [Foundation] High-Performance Tooling Setup
**Learning:** In an empty repository, the most impactful performance optimization is establishing high-performance development tooling immediately. Replacing legacy tools (flake8/black) with `ruff` from the start prevents technical debt and ensures fast CI/CD loops.
**Action:** Configured `pyproject.toml` with `ruff` for linting and formatting, targeting Python 3.12. Created standard `.gitignore` to prevent repository bloat.
