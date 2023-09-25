
n = int(input())
even = set()
odd = set()

for row in range(1, n+1):
    name = input()
    ascii_value = int(sum([ord(i) for i in name]) / row)

    if ascii_value % 2 == 0:
        even.add(ascii_value)

    else:
        odd.add(ascii_value)

if sum(odd) == sum(even):
    print(*even.union(odd), sep=", ")

elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")

else:
    print(*even.symmetric_difference(odd), sep=", ")

