# Sentinel Journal

## 2026-01-17 - Initial Repository Security Setup
**Vulnerability:** Absence of `.gitignore` in a new repository.
**Learning:** New repositories often start without environment restrictions, leading to accidental commitment of sensitive files (API keys, .env, virtual environments) and build artifacts.
**Prevention:** Always initialize a repository with a comprehensive `.gitignore` tailored to the tech stack (Python/Poetry) and project structure (data/models/cache) immediately upon creation.
