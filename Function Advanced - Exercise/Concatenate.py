def concatenate(*args, **kwargs):
    result = "".join(args)

    for key, element in kwargs.items():
        if key in result:
            result = result.replace(key, element)

    return result

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))