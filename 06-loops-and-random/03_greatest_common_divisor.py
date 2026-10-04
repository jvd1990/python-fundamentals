number_1 = int(input("Enter the first positive integer: "))
number_2 = int(input("Enter the second positive integer: "))

minimum = min(number_1, number_2)

for divisor in range(minimum, 0, -1):
    if number_1 % divisor == 0 and number_2 % divisor == 0:
        print("Greatest common divisor:", divisor)
        break