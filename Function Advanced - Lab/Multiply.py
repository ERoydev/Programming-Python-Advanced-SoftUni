
def multiply(*args):
    result = args[0]
    for i in range(1, len(args)):
        result *= args[i]

    return result

print(multiply(1, 4, 5))