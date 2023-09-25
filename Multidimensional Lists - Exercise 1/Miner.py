
def is_outside(row, col):
    return row < 0 or row >= n or col < 0 or col >= n

moves = {"left": (0, -1),
         "right": (0, +1),
         "up": (-1, 0),
         "down": (+1, 0)}

n = int(input())

commands = input().split()
start_row, start_col = 0, 0
matrix = []
coals = 0

for row in range(n):
    matrix.append(input().split())
    coals += matrix[row].count("c")
    if "s" in matrix[row]:
        start_row, start_col = row, matrix[row].index("s")

for command in commands:
    row_pos, col_pos = moves[command]
    current_row, current_col = row_pos + start_row, col_pos + start_col

    if is_outside(current_row, current_col):
        continue

    start_row, start_col = current_row, current_col
    if matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        raise SystemExit

    if matrix[current_row][current_col] == "c":
        matrix[current_row][current_col] = "*"
        coals -= 1
        if coals == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            raise SystemExit

print(f"{coals} pieces of coal left. ({current_row}, {current_col})")



