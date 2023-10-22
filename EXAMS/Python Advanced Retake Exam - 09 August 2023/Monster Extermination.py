from collections import deque


monsters_armor = deque([int(x) for x in input().split(",")])
soldier_damange = [int(x) for x in input().split(",")]
killed_monsters = 0

while monsters_armor and soldier_damange:
    current_armor = monsters_armor.popleft()
    current_soldier = soldier_damange.pop()

    if current_soldier >= current_armor:
        killed_monsters += 1
        current_soldier -= current_armor
        if current_soldier > 0:
            if soldier_damange:
                soldier_damange[-1] += current_soldier
                continue

            soldier_damange.append(current_soldier)

    else:
        current_armor -= current_soldier
        monsters_armor.append(current_armor)


if not monsters_armor:
    print("All monsters have been killed!")

if not soldier_damange:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
