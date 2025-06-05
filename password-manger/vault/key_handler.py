import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
    print(f"Key generated and saved to 'key.key'")

def ensure_key_exists():
    if not os.path.exists("key.key"):
        print("Key not found. Generating a new one...")
        generate_key()

def load_key():
    with open("key.key", "rb") as f:
        return f.read()
