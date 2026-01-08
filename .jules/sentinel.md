## 2024-05-24 - [Foundational Security in Empty Repositories]
**Vulnerability:** Missing `.gitignore` in a new repository.
**Learning:** In the "Phase 0" or empty state of a repository, the most critical security risk is the accidental commitment of sensitive files (secrets, environments, local configs) as developers begin setup.
**Prevention:** Establish a comprehensive `.gitignore` immediately upon repository initialization, before any code or configuration is added. This acts as a "security first" gate for all future contributions.
