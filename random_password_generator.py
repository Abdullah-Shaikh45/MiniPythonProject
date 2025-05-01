import random
import string


def generate_password():
    length = int(input("Enter the length of the password: ").strip())
    include_uppercase = input(
        "Include uppercase letters? (yes or no): ").strip().lower()
    include_special = input(
        "Include special characters? (yes or no): ").strip().lower()
    include_digits = input("Include digits? (yes or no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    all_character = lower + uppercase + special + digits

    if not all_character:
        print("You must include at least one character type.")
        return

    required_character = []

    if include_uppercase == "yes":
        required_character.append(random.choice(uppercase))

    if include_special == "yes":
        required_character.append(random.choice(special))

    if include_digits == "yes":
        required_character.append(random.choice(digits))

    remaining_length = length - len(required_character)
    password = required_character.copy()

    for _ in range(remaining_length):
        character = random.choice(all_character)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    print("Generated Password:", str_password)


generate_password()
