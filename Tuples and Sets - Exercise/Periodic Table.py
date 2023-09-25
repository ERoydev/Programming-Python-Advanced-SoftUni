
n = int(input())

table = set()

for i in range(n):
    elements = input().split()

    [table.add(subset) for subset in elements]

print(table)