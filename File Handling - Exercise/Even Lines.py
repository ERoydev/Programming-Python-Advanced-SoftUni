
replace = ["-", ",", ", ", ".", "!", "?"]

with open("text.txt", "r") as file:
    result = file.readlines()

    filtered = [result[i].strip() for i in range(len(result)) if i % 2 == 0]

    for i in replace:
        filtered[0] = filtered[0].replace(i, "@")
        filtered[1] = filtered[1].replace(i, "@")

    for i in filtered:
        print(" ".join(i.split()[::-1]))