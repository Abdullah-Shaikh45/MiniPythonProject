from .file_handler import load_vault, save_vault
from .encryptor import encrypt_password, decrypt_password

def add_entry(data):
    vault = load_vault()
    website = data["website"]
    vault[website] = {
        "username": data["username"],
        "password": encrypt_password(data["password"])
    }
    save_vault(vault)
    print(f"Saved entry for '{website}'.")

def view_entries():
    vault = load_vault()
    if not vault:
        print("Vault is empty.")
        return

    print("\nDecrypted Vault Data:")
    for site, creds in vault.items():
        print(f"\nWebsite: {site}")
        print(f"Username: {creds['username']}")
        print(f"Password: {decrypt_password(creds['password'])}")

def search_entry():
    vault = load_vault()
    term = input("Enter website to search: ").strip().lower()

    for site, creds in vault.items():
        if term in site.lower():
            print(f"\nWebsite: {site}")
            print(f"Username: {creds['username']}")
            print(f"Password: {decrypt_password(creds['password'])}")
            return
    print("No match found.")

def edit_entry():
    vault = load_vault()
    site = input("Enter website to edit: ").strip()

    if site not in vault:
        print(f"No entry for '{site}'")
        return

    current = vault[site]
    current_pass = decrypt_password(current['password'])

    new_user = input(f"Username [{current['username']}]: ").strip() or current['username']
    new_pass = input(f"Password [{current_pass}]: ").strip() or current_pass

    vault[site] = {
        "username": new_user,
        "password": encrypt_password(new_pass)
    }
    save_vault(vault)
    print(f"Entry for '{site}' updated.")

def delete_entry():
    vault = load_vault()
    site = input("Enter website to delete: ").strip()

    if site not in vault:
        print(f"No entry for '{site}'")
        return

    confirm = input(f"Are you sure? (y/n): ").lower()
    if confirm == 'y':
        del vault[site]
        save_vault(vault)
        print(f"Deleted '{site}'")
