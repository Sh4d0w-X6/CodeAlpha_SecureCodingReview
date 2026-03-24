# 🔐 Secure Coding Review Report

## 📌 Overview
This report analyzes security vulnerabilities in a simple login system.

## ❌ Identified Vulnerabilities

1. Hardcoded Credentials
- Username and password are stored in plain text.

2. No Password Encryption
- Password is not hashed or secured.

3. Lack of Input Validation
- User input is not validated or sanitized.

4. No Protection Against Brute Force
- Unlimited login attempts allowed.

## ✅ Recommendations

- Use hashed passwords (bcrypt)
- Store credentials securely in a database
- Validate and sanitize user input
- Implement login attempt limits
- Use authentication frameworks

## 📢 Conclusion
Secure coding practices are essential to prevent vulnerabilities and protect user data.