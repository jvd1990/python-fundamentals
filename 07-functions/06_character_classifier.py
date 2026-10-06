def classify_character(character):
    if "0" <= character <= "9":
        print("Your character is a digit.")
    elif "A" <= character <= "Z":
        print("Your character is an uppercase letter.")
    elif "a" <= character <= "z":
        print("Your character is a lowercase letter.")
    else:
        print("Your character is another symbol.")


character = input("Enter one character: ")
classify_character(character)