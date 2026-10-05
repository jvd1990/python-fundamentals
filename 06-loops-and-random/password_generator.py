import random
import string

# Educational password generator using random.sample().
# For real account passwords, use the secrets module.

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
symbols = string.punctuation
numbers = string.digits

all_characters = lowercase_letters + uppercase_letters + symbols + numbers

while True:
    print("\nPassword Generator")
    print("1. Generate a password")
    print("2. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        length_input = input("Enter the password length: ").strip()

        if not length_input.isascii() or not length_input.isdigit():
            print("Please enter a positive whole number.")
            continue

        length = int(length_input)

        if length < 1 or length > len(all_characters):
            print(f"Length must be between 1 and {len(all_characters)}.")
            continue

        selected_characters = random.sample(all_characters, length)
        password = "".join(selected_characters)

        print("Generated password:", password)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1 or 2.")

    print("-" * 40)