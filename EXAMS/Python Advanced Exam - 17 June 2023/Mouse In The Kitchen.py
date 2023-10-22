ROWS, COLS = [int(x) for x in input().split(",")]

matrix = []

for row in range(ROWS):
    matrix.append(list(input()))


while True:
    command = input()
    if command == "danger":
        break

    