def custom_sum(iterable):
    total = 0

    for number in iterable:
        total += number

    return total


print("List sum:", custom_sum([1, 5, 7, 6]))
print("Tuple sum:", custom_sum((2, 9, 10)))
print("Set sum:", custom_sum({3, 4, 8}))