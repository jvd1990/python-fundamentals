# Educational project: simple character encoding.
# This method is not secure encryption.

while True:
    print("\nSimple Encryption and Decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        plain_text = input("Enter your text: ")
        encrypted_text = ""

        for character in plain_text:
            code = ord(character) * 2 + 5
            encrypted_text += chr(code)

        print("Encrypted text:", encrypted_text)

    elif choice == "2":
        encrypted_text = input("Enter the encrypted text: ")
        plain_text = ""

        for character in encrypted_text:
            code = (ord(character) - 5) // 2
            plain_text += chr(code)

        print("Decrypted text:", plain_text)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

    print("-" * 40)