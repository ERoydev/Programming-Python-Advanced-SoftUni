def is_outside(row, col):
    return 0 > row or row >= SIZE or 0 > col or col >= SIZE


def check_if_give_position_is_empty(row, col):
    return matrix[row][col] == "."


def move(direction, steps):
    r = my_position[0] + (positions[direction][0] * steps)
    c = my_position[1] + (positions[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position

    if matrix[r][c] == "x":
        return my_position

    return [r, c]



my_position = []
targets_hit = 0
TOTAL_TARGETS = 0
SIZE = 5
matrix = []

positions = {"right": (0, 1),
             "left": (0, -1),
             "up": (-1, 0),
             "down": (1, 0)}

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(len(matrix[row])):
        if matrix[row][col] == "x":
            TOTAL_TARGETS += 1

        if matrix[row][col] == "A":
            my_position = [row, col]


n = int(input())
shooted_targets = []

matrix[my_position[0]][my_position[1]] = "."
for i in range(n):
    args = input().split()
    command = args[0]
    direction = args[1]

    if command == "move":
        steps = int(args[2])

        my_position = move(direction, steps)

    if command == "shoot":
        r = my_position[0] + positions[direction][0]
        c = my_position[1] + positions[direction][1]

        while 0 <= r < SIZE and 0 <= c < SIZE:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                shooted_targets.append([r, c])
                targets_hit += 1
                break

            r += positions[direction][0]
            c += positions[direction][1]

        if targets_hit == TOTAL_TARGETS:
            print(f"Training completed! All {TOTAL_TARGETS} targets hit.")
            break

else:
    print(f"Training not completed! {TOTAL_TARGETS - targets_hit} targets left.")

[print(row) for row in shooted_targets]


