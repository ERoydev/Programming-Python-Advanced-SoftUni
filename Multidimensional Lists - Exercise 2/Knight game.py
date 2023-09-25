
N = int(input())

def is_outside(row, col):
    return 0 > row or row >= N or 0 > col or col >= N

matrix = [[x for x in input()] for _ in range(N)]

positions = (
    (-2, -1), #up-left
    (-2, +1), #up-right,
    (+2, +1), #down-right,
    (+2, -1), #down-left
    (-1, +2), #left-up
    (+1, +2), #left-down
    (-1, -2), #right-up
    (+1, -2), #right-down
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(N):
        for col in range(N):
            if matrix[row][col] == "K":
                attacks = 0
                for pos in positions:
                    curr_row= row + pos[0]
                    curr_col = col + pos[1]
                    if is_outside(curr_row, curr_col):
                        continue

                    if matrix[curr_row][curr_col] == "K":
                        attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_pos = [(row, col)]

    if max_attacks == 0:
        break

    most_row, most_col = knight_with_most_attacks_pos[0]
    matrix[most_row][most_col] = 0
    removed_knights += 1


print(removed_knights)
