import json
import os

def load_vault(path="vault.json"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_vault(vault, path="vault.json"):
    with open(path, "w") as f:
        json.dump(vault, f, indent=2)
