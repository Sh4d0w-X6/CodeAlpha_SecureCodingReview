import hashlib

# Stored username and hashed password
stored_username = "admin"
stored_password = hashlib.sha256("1234".encode()).hexdigest()

# Login attempts limit
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Hash the entered password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and hashed_password == stored_password:
        print("Login successful")
        break
    else:
        print("Login failed")
        attempts += 1

if attempts == max_attempts:
    print("Too many failed attempts. Access blocked.")