height = int(input("Enter the triangle height: "))

for row in range(1, height + 1):
    print(" " * (height - row), end="")
    print("*" * row)