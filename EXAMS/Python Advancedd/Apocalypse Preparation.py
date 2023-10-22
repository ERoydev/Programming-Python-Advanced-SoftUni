from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items = {
    30: {"name": "Patch", "quantity": 0},
    40: {"name": "Bandage", "quantity": 0},
    100: {"name": "MedKit", "quantity": 0},
}

while textile and medicaments:
    current_textile = textile.popleft()
    current_medicament = medicaments.pop()

    result = current_textile + current_medicament

    if result in items.keys():
        items[result]['quantity'] += 1

    elif result > 100:
        items[100]['quantity'] += 1
        medicaments[-1] += (result - 100)

    else:
        medicaments.append(current_medicament + 10)

if not textile and not medicaments:
    print(f"Textiles and medicaments are both empty.")

else:
    print("Textiles are empty.") if not textile else None
    print("Medicaments are empty.") if not medicaments else None

for key, value in sorted(items.items(), key=lambda x: (-x[1]['quantity'], x[1]['name'])):
    if value['quantity'] > 0:
        print(f"{value['name']} - {value['quantity']}")


if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textile:
    print(f"Textiles left: {', '.join(str(x) for x in textile)}")