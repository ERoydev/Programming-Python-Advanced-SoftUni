
def is_outside(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

ROWS, COLS = [int(x) for x in input().split()]
matrix = []

touched_opponents = 0
count_moves = 0

for row in range(ROWS):
    matrix.append([x for x in input().split()])
    if "B" in matrix[row]:
        start_row, start_col = row, matrix[row].index("B")

matrix[start_row][start_col] = "-"
while True:
    command = input()
    if command == "Finish":
        break

    curr_row, curr_col = start_row + moves[command][0], start_col + moves[command][1]

    if is_outside(curr_row, curr_col):
        continue

    if matrix[curr_row][curr_col] == "O":
        continue

    if matrix[curr_row][curr_col] == "P":
        touched_opponents += 1
        matrix[curr_row][curr_col] = "-"


    start_row, start_col = curr_row, curr_col
    count_moves += 1

    if touched_opponents == 3:
        break


print(f"Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {count_moves}")