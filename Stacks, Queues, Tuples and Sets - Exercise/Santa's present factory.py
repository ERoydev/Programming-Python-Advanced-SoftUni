from collections import deque

materials = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

crafted = False

present_price = {150: "Doll",
                 250: "Wooden train",
                300: "Teddy bear",
                400: "Bicycle"}

stash = {"Doll": 0,
         "Wooden train": 0,
         "Teddy bear": 0,
         "Bicycle": 0}

while materials and magic_values:
    if (stash["Doll"] > 0 and stash["Wooden train"] > 0) or (stash["Teddy bear"] > 0 and stash["Bicycle"] > 0):
        crafted = True

    current_box = materials.pop()
    current_magic = magic_values.popleft()

    result = current_box * current_magic

    if result in present_price:
        item = present_price[result]
        stash[item] += 1
        continue

    if result < 0:
        values = current_box + current_magic
        materials.append(values)

    elif result > 0:
        current_box += 15
        materials.append(current_box)

    elif current_box == 0 and current_magic == 0:
        continue

    elif current_box == 0:
        magic_values.appendleft(current_magic)

    elif current_magic == 0:
        materials.append(current_box)


if crafted:
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(stash.items(), key=lambda x: x[0]):
    if value > 0:
        print(f"{key}: {value}")