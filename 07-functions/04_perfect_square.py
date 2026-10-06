def check_perfect_square(number):
    for candidate in range(0, number + 1):
        if candidate ** 2 == number:
            print(f"Yes: {candidate} × {candidate} = {number}")
            break
    else:
        print("No: the number is not a perfect square.")


number = int(input("Enter an integer: "))
check_perfect_square(number)