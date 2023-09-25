
n = int(input())
data = set()

for i in range(n):
    name = input()
    data.add(name)

print(*data, sep="\n")