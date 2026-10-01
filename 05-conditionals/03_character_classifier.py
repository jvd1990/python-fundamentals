character = input("Enter one character: ")

ascii_value = ord(character)

if 48 <= ascii_value <= 57:
    print("The character is a digit.")
elif 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
    print("The character is an English letter.")
else:
    print("The character is something else.")