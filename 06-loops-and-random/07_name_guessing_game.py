from random import choice

names = [
    "Ali",
    "Sara",
    "Reza",
    "Mina",
    "Javad",
    "Maryam",
    "Amir",
    "Neda",
    "Omid",
    "Leila"
]

remaining_names = names.copy()

print("Choose a name from this list and keep it in your mind:")
print(", ".join(names))

while True:
    if len(remaining_names) == 0:
        print("There are no names left to guess.")
        break

    computer_guess = choice(remaining_names)

    answer = input(
        f"Is your name {computer_guess}? (yes/no): "
    )

    if "y" in answer.lower():
        print("The name was found!")
        break

    remaining_names.remove(computer_guess)