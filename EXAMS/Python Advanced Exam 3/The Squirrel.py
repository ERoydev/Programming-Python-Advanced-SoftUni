
def is_outside(row, col):
    return 0 > row or row >= len(matrix) or 0 > col or col >= len(matrix[0])

moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

field_length = int(input())
commands = input().split(", ")

matrix = []
hazelnuts = 3

for row in range(field_length):
    matrix.append(list(input()))
    if "s" in matrix[row]:
        start_row, start_col = row, matrix[row].index("s")

matrix[start_row][start_col] = "*"
for move in commands:
    curr_row, curr_col = start_row + moves[move][0], start_col + moves[move][1]

    if is_outside(curr_row, curr_col):
        print(f"The squirrel is out of the field.")
        print(f"Hazelnuts collected: {3 - hazelnuts}")
        raise SystemExit

    if matrix[curr_row][curr_col] == "h":
        hazelnuts -= 1
        matrix[curr_row][curr_col] = "*"

    if matrix[curr_row][curr_col] == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {3 - hazelnuts}")
        raise SystemExit

    start_row, start_col = curr_row, curr_col

if hazelnuts == 0:
    print(f"Good job! You have collected all hazelnuts!")

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {3 - hazelnuts}")