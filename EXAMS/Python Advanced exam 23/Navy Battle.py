SIZE = int(input())

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
health = 3
cruisers = 3

for row in range(SIZE):
    matrix.append([x for x in input()])
    if "S" in matrix[row]:
        start_row, start_col = row, matrix[row].index("S")

matrix[start_row][start_col] = "-"
while True:
    move = input()
    curr_row, curr_col = start_row + moves[move][0], start_col + moves[move][1]

    if matrix[curr_row][curr_col] == "*":
        health -= 1
        matrix[curr_row][curr_col] = "-"
        start_row, start_col = curr_row, curr_col

        if health == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{start_row}, {start_col}]!")
            break

    elif matrix[curr_row][curr_col] == "C":
        matrix[curr_row][curr_col] = "-"
        cruisers -= 1
        start_row, start_col = curr_row, curr_col

        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    start_row, start_col = curr_row, curr_col

matrix[start_row][curr_col] = "S"
for row in matrix:
    print(*row, sep="")