def custom_maximum(*args):
    maximum = args[0]

    for number in args:
        if number > maximum:
            maximum = number

    return maximum


print(custom_maximum(1000, 11, 2, 500, -42, 0, 256))
print(custom_maximum(-8, -3, -12))