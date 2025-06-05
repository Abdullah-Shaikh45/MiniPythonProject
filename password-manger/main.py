from vault.key_handler import ensure_key_exists
from vault.operations import add_entry, view_entries, search_entry, edit_entry, delete_entry

def get_user_input():
    site = input("Website: ").strip()
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()

    if not site or not user or not pwd:
        print("All fields are required.")
        return None

    return {"website": site, "username": user, "password": pwd}

def menu():
    ensure_key_exists()

    while True:
        print("\n====== Password Manager ======")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Search password")
        print("4. Edit password")
        print("5. Delete password")
        print("6. Exit")

        choice = input("Choose (1-6): ").strip()

        match choice:
            case "1":
                data = get_user_input()
                if data:
                    add_entry(data)

            case "2":
                view_entries()

            case "3":
                search_entry()

            case "4":
                edit_entry()

            case "5":
                delete_entry()

            case "6":
                print("Exiting...")
                break

            case _:
                print("Invalid option. Please choose between 1 to 6.")

if __name__ == "__main__":
    menu()
