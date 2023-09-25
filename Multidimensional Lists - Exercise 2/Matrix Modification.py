
def is_invalid(row, col):
    return 0 > row or row >= ROWS or 0 > col or col >= ROWS


ROWS = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(ROWS)]

while True:
    user_input = input()
    if user_input == "END":
        break

    args = user_input.split()
    command = args[0]
    row, col = int(args[1]), int(args[2])
    value = int(args[3])

    if is_invalid(row, col):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    elif command == "Subtract":
        matrix[row][col] -= value


for row in matrix:
    print(*row)