from collections import deque

food_quantity = int(input())

sequence = deque([int(x) for x in input().split()])
print(max(sequence))
served = True

while sequence:
    order = sequence.popleft()

    if order > food_quantity:
        sequence.appendleft(order)
        print(f"Orders left: {' '.join(str(x) for x in sequence)}")
        served = False
        break

    food_quantity -= order

if served:
    print("Orders complete")




