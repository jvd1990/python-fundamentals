number = int(input("Enter an integer: "))

number = abs(number)

if number == 0:
    digit_count = 1
else:
    digit_count = 0

    while number > 0:
        number //= 10
        digit_count += 1

print("Number of digits:", digit_count)