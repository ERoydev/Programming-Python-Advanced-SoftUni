def mark_visited(row, col):
    matrix[row][col] = "*"

def is_outside(row, col):
    return 0 > row or row >= size or 0 > col or col >= size

def is_rabbit_hole(row, col):
    return matrix[row][col] == "R"

def check_if_number(row, col):
    return matrix[row][col] == "." or matrix[row][col] == "*"

def get_alice_position():
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "A":
                return row, col

moves = {"down": (1, 0),
         "up": (-1, 0),
         "left": (0, -1),
         "right": (0, 1)}


BAGS_TO_COLLECT = 10
size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]


alice_row, alice_col = get_alice_position()
collected = 0
matrix[alice_row][alice_col] = "*"
failed = False

while collected < BAGS_TO_COLLECT:
    command = input()
    row, col = moves[command]
    curr_row, curr_col = alice_row + row, alice_col + col

    if is_outside(curr_row, curr_col):
        failed = True
        break

    if is_rabbit_hole(curr_row, curr_col):
        mark_visited(curr_row, curr_col)
        failed = True
        break

    if not check_if_number(curr_row, curr_col):
        collected += matrix[curr_row][curr_col]

    mark_visited(curr_row, curr_col)
    alice_row, alice_col = curr_row, curr_col


if collected >= BAGS_TO_COLLECT:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]