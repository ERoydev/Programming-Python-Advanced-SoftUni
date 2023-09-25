
n = int(input())
max_length = float('-inf')
final = None

for i in range(n):
    first, second = input().split("-")

    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(",")]

    first_set = {i for i in range(first_start, first_end+1)}
    second_set = {i for i in range(second_start, second_end+1)}

    result = first_set.intersection(second_set)

    if len(result) > max_length:
        final = result
        max_length = len(final)

print(f"Longest intersection is {[el for el in final]} with length {max_length}")