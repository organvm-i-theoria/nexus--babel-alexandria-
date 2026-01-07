## 2026-01-07 - [Foundational Security in Empty Repos]
**Vulnerability:** Missing `.gitignore` allows accidental commit of secrets (e.g., `.env`, keys) and build artifacts.
**Learning:** In a new/empty repository, the most impactful security enhancement is not adding scanning tools (which have nothing to scan), but establishing a secure baseline configuration.
**Prevention:** Always initialize `.gitignore` with strict exclusion rules for sensitive files before any code is written.
