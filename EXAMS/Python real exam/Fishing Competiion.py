def is_outside(row, col):
    return row < 0 or row >= n or col < 0 or col >= n

n = int(input())

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

fish_count = 0
matrix = []
for row in range(n):
    matrix.append([x for x in input()])
    if "S" in matrix[row]:
        start_row, start_col = row, matrix[row].index("S")

matrix[start_row][start_col] = "-"
while True:
    command = input()
    if command == 'collect the nets':
        break

    curr_row, curr_col = start_row + moves[command][0], start_col + moves[command][1]

    if is_outside(curr_row, curr_col):
        if curr_col >= n:
            curr_col = 0

        elif curr_col < 0:
            curr_col = n - 1

        if curr_row >= n:
            curr_row = 0

        elif curr_row < 0:
            curr_row = n - 1


    if matrix[curr_row][curr_col].isdigit():
        fish_count += int(matrix[curr_row][curr_col])
        matrix[curr_row][curr_col] = "-"


    elif matrix[curr_row][curr_col] == "W":
        start_row, start_col = curr_row, curr_col
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{start_row},{start_col}]")
        raise SystemExit

    start_row, start_col = curr_row, curr_col

matrix[start_row][start_col] = "S"

if fish_count >= 20:
    print("Success! You managed to reach the quota!")

else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_count} tons of fish more.")

if fish_count > 0:
    print(f"Amount of fish caught: {fish_count} tons.")

[print(*row, sep="") for row in matrix]