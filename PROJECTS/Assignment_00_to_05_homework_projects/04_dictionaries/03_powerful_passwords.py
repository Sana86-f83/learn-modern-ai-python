# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)

import hashlib

# ANSI color codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

# Program heading
print(f"\n\t\t\t\t{BOLD}{CYAN}--------------------------------------")
print(f"\t\t\t\t{BOLD}{CYAN}      🔐 Secure Login System 🔐")
print(f"\t\t\t\t{BOLD}{CYAN}--------------------------------------{RESET}\n")

def hash_password(password):
    """
    Hashes the password using SHA256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary storing emails and their hashed passwords
stored_logins = {
    "user@example.com": hash_password("hello"),  # Hashed 'hello'
    "test@domain.com": hash_password("password"), # Hashed 'password'
    "sana@example.com":hash_password("sanaumer")  # Hashed 'sanaumer'
}

def login(email, password_to_check):
    """
    This function checks if the password_to_check matches the stored hashed password for the given email.

    Args:
    - email (str): The email to check.
    - password_to_check (str): The password to check.

    Returns:
    - bool: True if the password matches, False otherwise.
    """
    if email in stored_logins:
        hashed_password = hash_password(password_to_check)
        
        if hashed_password == stored_logins[email]:
            print(f"\t\t\t\t{GREEN}{BOLD}✅ Login successful! Welcome, {email}.{RESET}\n")
            return True
        else:
            print(f"\t\t\t\t\t\t{RED}{BOLD}❌ Incorrect password. Please try again.{RESET}\n")
            return False
    else:
        print(f"\t\t\t\t\t{YELLOW}{ITALIC}⚠️  Email not found. Please register first.{RESET}\n")
        return False

# Testing the function
print(f"\t\t\t\t\t{BOLD}{ITALIC}🔍 Testing Login System...{RESET}\n")
login("user@example.com", "hello")  # Expected output: Success ✅
login("user@example.com", "wrongpassword")  # Expected output: Incorrect ❌
login("test@domain.com", "password")  # Expected output: Success ✅
login("unknown@domain.com", "test")  # Expected output: Email not found ⚠️
login("sana@example.com","sanaumer") # Expected output: Success ✅