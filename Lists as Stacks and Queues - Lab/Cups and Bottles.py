from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
filled_bottles = [int(x) for x in input().split()]

left_water = 0

while True:
    if not cups_capacity or not filled_bottles:
        break

    cup = cups_capacity.popleft()
    bottle = filled_bottles.pop()

    if cup > bottle:
        cup -= bottle
        cups_capacity.appendleft(cup)

    else:
        left_water += bottle - cup

if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")

else:
    print(f"Bottles: {' '.join(str(x) for x in filled_bottles)}")

print(f"Wasted litters of water: {left_water}")