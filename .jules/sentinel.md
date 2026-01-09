## 2024-01-09 - [Repository Initialization Security]
**Vulnerability:** Empty repositories lack default protections against secret leakage, increasing the risk of developers accidentally committing `.env` files or keys during initial setup.
**Learning:** Security must be "baked in" from Phase 0. A `.gitignore` file acts as the first line of defense before any code is written.
**Prevention:** Always initialize new repositories with a comprehensive `.gitignore` that explicitly blocks common secret patterns (`.env`, `*.key`, `secrets.json`) and environment artifacts.
