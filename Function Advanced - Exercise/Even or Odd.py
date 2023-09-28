
def even_odd(*args):
    command = list(args).pop()
    if command == "even":
        result = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, args))

    else:
        result = [int(x) for x in args if isinstance(x, int) and x % 2 != 0]

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
