# Security Policy

## Supported Versions

As this project is in Phase 0 (pre-alpha), no versions are currently supported for security updates. However, we take security seriously from the start.

| Version | Supported          |
| ------- | ------------------ |
| 0.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We strongly encourage you to report potential security vulnerabilities to our team.

### Process

1.  **Do not** open a public issue on GitHub.
2.  Email details to `security@example.com` (Replace with actual security contact when available).
3.  Include a description of the vulnerability and steps to reproduce.

### Response

-   We will acknowledge your report within 48 hours.
-   We will provide an estimated timeline for the fix.
-   We will notify you when the fix is released.

## Security Tools

This repository uses the following tools to ensure code security:

-   **Bandit**: Scans for common security issues in Python code.
-   **Safety**: Checks dependencies for known security vulnerabilities.

Run security checks with:

```bash
bandit -r .
safety check
```

## Best Practices

-   Never commit secrets or API keys.
-   Always sanitize user inputs.
-   Follow the Principle of Least Privilege.
