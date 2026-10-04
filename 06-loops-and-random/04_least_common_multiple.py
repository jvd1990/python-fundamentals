number_1 = int(input("Enter the first positive integer: "))
number_2 = int(input("Enter the second positive integer: "))

minimum = min(number_1, number_2)
maximum = max(number_1, number_2)

multiple = maximum

while multiple % minimum != 0:
    multiple += maximum

print("Least common multiple:", multiple)