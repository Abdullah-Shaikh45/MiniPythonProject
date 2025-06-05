from cryptography.fernet import Fernet
from .key_handler import load_key

def get_fernet():
    key = load_key()
    return Fernet(key)

def encrypt_password(password):
    fernet = get_fernet()
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    fernet = get_fernet()
    return fernet.decrypt(encrypted_password.encode()).decode()

