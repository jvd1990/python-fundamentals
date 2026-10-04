number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

minimum = min(number_1, number_2)
maximum = max(number_1, number_2)

for number in range(minimum, maximum + 1):
    print(number)