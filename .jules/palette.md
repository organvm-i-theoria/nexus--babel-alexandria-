## 2026-01-14 - Standardizing Project Entry Points
**Learning:** Developers struggle to navigate repositories with unwieldy filenames (containing spaces, special chars) and missing entry points (`README.md`). This increases cognitive load and friction for terminal users.
**Action:** Always sanitize filenames to be shell-friendly (kebab-case/snake_case) and ensure a `README.md` exists to guide new contributors immediately.
