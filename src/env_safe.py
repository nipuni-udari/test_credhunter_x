"""Safe runtime secret loading examples."""

import os

# EXPECTED: IGNORED — safe environment-variable references
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
SERVICE_API_KEY = os.environ.get("SERVICE_API_KEY", "")
