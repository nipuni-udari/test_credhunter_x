"""Synthetic high-risk examples for CredHunter-X."""

# EXPECTED: HIGH or CRITICAL / FAIL — synthetic database URL with embedded password
DATABASE_URL = "chx-postgres://orders_svc:CHX_DB_PASS_R8mN7qP2xL@orders-db.internal:5432/orders"

# EXPECTED: HIGH / FAIL — synthetic Stripe-like live key, not real sk_live_
STRIPE_LIVE_KEY = "CHX_STRIPE_LIVE_SECRET_4K7N2Q9V5X8B1M6P3R0T"
