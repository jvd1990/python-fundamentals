number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

limit = min(number_1, number_2)

print("Common divisors:")

for divisor in range(1, limit + 1):
    if number_1 % divisor == 0 and number_2 % divisor == 0:
        print(divisor)