"""Synthetic critical examples for CredHunter-X.
These are NOT real provider credentials and should not trigger GitHub Push Protection.
"""

# EXPECTED: CRITICAL / FAIL — synthetic GitHub-like token, not a real ghp_ token
GITHUB_TOKEN = "CHX_GITHUB_PAT_7H4D2N9QX5R8M1P0Z3V6B9C2F"

# EXPECTED: CRITICAL / FAIL — synthetic OpenAI-like key, not a real sk- key
OPENAI_API_KEY = "CHX_OPENAI_PROJECT_KEY_9F2D7A4C1B8E5H3K6M0P2R9T"

# EXPECTED: CRITICAL or HIGH / FAIL — synthetic AWS-like access key, not real AKIA/ASIA
AWS_ACCESS_KEY_ID = "CHX_AWS_ACCESS_KEY_ID_5N8Q1T4W7Y0U3I6O9P2S"
