number = int(input("Enter an integer: "))

number = abs(number)
digit_count = 0

if number == 0:
    digit_count = 1

while number > 0:
    number //= 10
    digit_count += 1

print("Number of digits:", digit_count)