number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

multiple = max(number_1, number_2)

while True:
    if multiple % number_1 == 0 and multiple % number_2 == 0:
        break

    multiple += 1

print("Least common multiple:", multiple)