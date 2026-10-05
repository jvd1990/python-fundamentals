import time
import os

while True:
    choice = input(
        "\nDo you want to start the timer? (y/n): "
    ).strip().lower()

    if choice in ("y", "yes"):
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if hours < 0 or minutes < 0 or seconds < 0:
            print("Please enter non-negative values.")
            continue

        print("Timer starts now!")
        time.sleep(1)

        while total_seconds > 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("Seconds remaining:", total_seconds)

            time.sleep(1)
            total_seconds -= 1

        print("Timer ended!")

    elif choice in ("n", "no"):
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter y or n.")