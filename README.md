# CredHunter-X Push-Safe Severity Test Project

This is a compact synthetic project for testing CredHunter-X without triggering GitHub Push Protection.

Important: The values are NOT real provider tokens. They use `CHX_...` synthetic prefixes and are detected by the included `.gitleaks.toml` rules.

Expected behaviour:

- Critical/high synthetic credentials are reported and block when `fail_on: high`.
- Medium/warn credentials are reported as warnings or non-blocking findings.
- Low/dev values should not block.
- Placeholders and environment-variable examples should be ignored.
- Reports are uploaded before the final workflow failure.

Do not replace these synthetic values with real tokens.
