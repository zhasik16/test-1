# More security issues for AI to find
DB_CONFIG = {
    "host": "localhost",
    "user": "admin",
    "password": "database_password_123",  # 🔴 CRITICAL
    "name": "production_db"
}

AWS_KEYS = {
    "access_key": "AKIAIOSFODNN7EXAMPLE",
    "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # 🔴 CRITICAL
}

# API endpoints with keys
STRIPE_API_KEY = "sk_test_1234567890"
SENDGRID_API_KEY = "SG.1234567890"
