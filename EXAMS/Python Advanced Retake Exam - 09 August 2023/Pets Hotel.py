def get_return_info(failed, result, capacity, data):
    if not failed:
        result += f"All pets are accommodated! Available capacity: {capacity}."

    result += "\nAccommodated pets:"
    for name, count in sorted(data.items()):
        result += f"\n{name}: {count}"

    return result



def accommodate_new_pets(capacity: int, weight_limit: float, *args):
    data = {}
    failed = False
    result = ""

    for element in args:
        name, weight = element

        if capacity == 0:
            result += "You did not manage to accommodate all pets!"
            failed = True
            break

        if weight > weight_limit:
            continue

        data[name] = data.get(name, 0)
        data[name] += 1
        capacity -= 1

    return get_return_info(failed, result, capacity, data)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))