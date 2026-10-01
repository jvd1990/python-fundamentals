number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

while number_2 != 0:
    number_1, number_2 = number_2, number_1 % number_2

print("Greatest common divisor:", abs(number_1))