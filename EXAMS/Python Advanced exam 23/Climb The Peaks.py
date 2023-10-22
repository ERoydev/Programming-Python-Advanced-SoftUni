from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

mountains = {
    80: ["Vihren", False],
    90: ["Kutelo", False],
    100: ["Banski Suhodol", False],
    60: ["Polezhan", False],
    70: ["Kamenitza", False]

}

levels = deque([80, 90, 100, 60, 70])

while food_portions and stamina:
    if len(levels) == 0:
        break

    curr_food = food_portions.pop()
    curr_stamina = stamina.popleft()
    curr_level = levels.popleft()

    result = curr_stamina + curr_food

    if result >= curr_level:
        mountains[curr_level][1] = True
        continue

    else:
        levels.appendleft(curr_level)



if len(levels) == 0:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")


climbed = [value[0] for key, value in mountains.items() if value[1]]

if climbed:
    print("Conquered peaks:")
    for value in climbed:
        print(value)