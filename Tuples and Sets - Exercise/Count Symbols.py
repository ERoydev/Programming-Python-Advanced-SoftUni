
text = input()
data = set()

for i in text:
    data.add(f"{i}: {text.count(i)} time/s")


[print(el) for el in sorted(data)]