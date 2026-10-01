import random

names = ["Ali", "Sara", "Reza", "Mina", "Javad"]

secret_name = input("Choose a name from the list: ")

remaining_names = names.copy()

while remaining_names:
    guess = random.choice(remaining_names)
    remaining_names.remove(guess)

    print("Computer's guess:", guess)

    if guess.lower() == secret_name.lower():
        print("The name was found!")
        break
else:
    print("The name is not in the list.")