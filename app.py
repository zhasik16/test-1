import os
import requests

# 🔴 CRITICAL: Hardcoded secrets
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "super_secret_123"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

# User data processing function
def process_user_profile():
    # 🔴 HIGH: PII data in variables
    user_email = "john.doe@gmail.com"
    user_phone = "+1234567890"
    user_address = "123 Main St, New York, NY"
    
    # 🔴 CRITICAL: Printing PII to console
    print(user_email)
    print(f"User phone: {user_phone}")
    
    # 🟡 MEDIUM: User data in logs
    logger.info(f"Processing user: {user_email}")
    console.log(user_data)
    
    return True

# Payment processing with security issues
def process_payment(amount):
    # 🔴 CRITICAL: Credit card data
    credit_card = "4111-1111-1111-1111"
    cvv = "123"
    
    # 🔴 HIGH: Printing payment info
    print(f"Charging card: {credit_card}")
    
    # API call with exposed credentials
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "API-Key": API_KEY
    }
    
    response = requests.post(
        "https://api.payment.com/charge",
        headers=headers,
        json={"card": credit_card, "amount": amount}
    )
    
    return response.json()

# User authentication with issues
def login_user(username, password):
    # 🔴 CRITICAL: Plaintext password logging
    print(f"Login attempt: {username} with password: {password}")
    
    # 🔴 HIGH: Hardcoded admin credentials
    if username == "admin" and password == "admin123":
        return True
    
    return False

# Data export function
def export_user_data():
    users = [
        {"name": "Alice", "email": "alice@yahoo.com", "ssn": "123-45-6789"},
        {"name": "Bob", "email": "bob@gmail.com", "ssn": "987-65-4321"}
    ]
    
    # 🔴 HIGH: Exporting sensitive data without protection
    for user in users:
        print(f"Exporting: {user['name']} - {user['email']} - SSN: {user['ssn']}")
    
    return users

# Environment variables (the RIGHT way)
def proper_implementation():
    db_host = os.getenv("DB_HOST", "localhost")
    api_key = os.getenv("API_KEY")  # ✅ Good - using environment variables
    
    return f"Connected to {db_host}"

# Test the functions
if __name__ == "__main__":
    process_user_profile()
    process_payment(100.50)
    login_user("admin", "admin123")
    export_user_data()
    proper_implementation()
