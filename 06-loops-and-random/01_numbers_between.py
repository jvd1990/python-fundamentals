start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

if start > end:
    start, end = end, start

for number in range(start + 1, end):
    print(number)