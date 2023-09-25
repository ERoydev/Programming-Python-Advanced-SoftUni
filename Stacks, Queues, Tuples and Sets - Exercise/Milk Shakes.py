from collections import deque


def check_if_zero_or_negative(n):
    return n <= 0


chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(", ")])

prepared = 0

while chocolates and cups_of_milk and prepared != 5:
    current_chocolate = chocolates.pop()
    current_cup = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue

    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue

    elif current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        prepared += 1

    else:
        cups_of_milk.append(current_cup)
        chocolates.append(current_chocolate - 5)


print(f"Not enough milkshakes.") if prepared < 5 else print(f"Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(str(x) for x in chocolates)}") if chocolates else print(f"Chocolate: empty")

print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}") if cups_of_milk else print(f"Milk: empty")




