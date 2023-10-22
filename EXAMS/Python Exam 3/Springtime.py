
def start_spring(**kwargs):
    result = {}
    output = ""

    for key, value in kwargs.items():
        result[value] = result.get(value, [])
        result[value].append(key)

    for key, value in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{key}:\n"
        output += '\n'.join(f"-{x}" for x in sorted(value))
        output += "\n"

    return output.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))