
elements = input().split("|")[::-1]

elements = [el.strip() for el in elements]
result = []

for el in elements:
    result.append(el.split())

for i in result:
    for el in i:
        print(el, end=" ")