
seq = [int(x) for x in input().split()]
rack_capacity = int(input())
number_racks = 0
current_rack = 0

while seq:
    item = seq.pop()

    if (item + current_rack) > rack_capacity:
        current_rack = 0
        number_racks += 1
        seq.append(item)
        continue

    current_rack += item

if current_rack:
    number_racks += 1

print(number_racks)



