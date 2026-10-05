import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    user_input = int(input("Enter a number between 1 and 20: "))
    attempts += 1

    if user_input == secret_number:
        print("You guessed the number correctly!")
        print(f"Number of attempts: {attempts}")
        break
    elif user_input < secret_number:
        print("Your guess is too low. Please try again.")
    elif user_input > secret_number:
        print("Your guess is too high. Please try again.")