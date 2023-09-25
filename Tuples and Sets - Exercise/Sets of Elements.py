
n, m = [int(x) for x in input().split()]

first = set()
second = set()

for i in range(n):
    first.add(int(input()))

for i in range(m):
    second.add(int(input()))

print(*first.intersection(second), sep="\n")