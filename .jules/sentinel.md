## 2024-03-21 - [Initial Security Configuration]
**Vulnerability:** Absence of `.gitignore` in a new repository poses a high risk of accidental secret leakage (e.g., `.env`, private keys) and environment pollution.
**Learning:** Foundational security controls must be established *before* code development begins to prevent "secret sprawl."
**Prevention:** Implemented a comprehensive `.gitignore` covering Python, Node.js, and standard secret patterns.
