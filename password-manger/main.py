import json
import os
from cryptography.fernet import Fernet

# 1. Generate a key (only once — comment out after first run)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
    print(f"Key generated and saved to 'key.key': {key.decode()}")


# 2. Load the key from file
def load_key():
    with open("key.key", "rb") as f:
        return f.read()

# Save 'Encrypted Data' to a JSON File
def save_to_vault(data):
    file_path = "vault.json"

    if os.path.exists(file_path):
        print("Yes it exits!")
        with open(file_path, 'r') as f:
            vault = json.load(f)
    else:
        vault = {}

    website = data["website"]
    vault[website] = {
        "username": data["username"],
        "password": data["password"]
    }

    with open(file_path, 'w') as f:
        json.dump(vault, f, indent=2)

    print(f"\n Data saved to {file_path}")

# 3. Collect user data
def user_input():
    website = input("Enter the name of the website: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()

    if not website or not username or not password:
        print("Please fill all of the fields before proceeding!")
        return None

    return {
        "website": website,
        "username": username,
        "password": password,
    }


# ========== MAIN PROGRAM ==========

# Only run this once, then comment it out
# generate_key()
user_data = user_input()

if user_data:
    key = load_key()
    fernet = Fernet(key)

    # Encrypt password
    encrypted_password = fernet.encrypt(user_data["password"].encode())
    user_data["password"] = encrypted_password.decode()  # store as string

    print("\nEncrypted User Data:")
    print(user_data)

    save_to_vault(user_data)