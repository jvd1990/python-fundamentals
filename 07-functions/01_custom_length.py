def custom_length(iterable):
    counter = 0

    for _ in iterable:
        counter += 1

    return counter


text = "Hello Python"
numbers = [1, 2, 3, 4, 5]
letters = ("a", "b", "c")

print("Text length:", custom_length(text))
print("List length:", custom_length(numbers))
print("Tuple length:", custom_length(letters))