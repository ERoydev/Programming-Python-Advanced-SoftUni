from collections import deque

def is_outside(row, col):
    return 0 > row or row >= ROWS or 0 > col or col >= COLS

def print_matrix():
    [print(''.join(row)) for row in matrix]

def expand_bunnies():
    result = deque()
    while bunnies:
        bunny = bunnies.popleft()
        for move in moves.keys():
            row, col = moves[move]
            curr_row, curr_col = row + bunny[0], col + bunny[1]

            if is_outside(curr_row, curr_col):
                continue

            matrix[curr_row][curr_col] = "B"
            result.append((curr_row, curr_col))

    return result


moves = {"L": (0, -1),
         "R": (0, +1),
         "D": (+1, 0),
         "U": (-1, 0)}

ROWS, COLS = [int(x) for x in input().split()]

matrix = []
bunnies = deque([])
player_row, player_col = 0, 0

for row in range(ROWS):
    matrix.append([x for x in input()])

    for col in range(COLS):
        if matrix[row][col] == "B":
            bunnies.append((row, col))

        if matrix[row][col] == "P":
            player_row, player_col = row, col


commands = deque([x for x in input()])
current_row, current_col = player_row, player_col

matrix[player_row][player_col] = "."
while moves:
    row_pos, col_pos = moves[commands.popleft()]
    current_row, current_col = player_row + row_pos, col_pos + player_col

    bunnies = expand_bunnies()

    if is_outside(current_row, current_col):
        print_matrix()
        print(f"won: {player_row} {player_col}")
        break

    if matrix[current_row][current_col] == "B":
        print_matrix()
        print(f"dead: {current_row} {current_col}")
        break

    player_row, player_col = current_row, current_col
