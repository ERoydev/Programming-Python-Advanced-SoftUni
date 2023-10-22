def print_matrix():
    [print(*row, sep="") for row in matrix]

def check_if_pizza_delivered(row, col):
    return matrix[row][col] == "A"

def check_if_restaurant(row, col):
    return matrix[row][col] == "P"


def check_obstacle(row, col):
    return matrix[row][col] == "*"


def is_outside(row, col):
    return 0 > row or row >= ROWS or 0 > col or col >= COLS


ROWS, COLS = [int(x) for x in input().split()]
matrix = []
directions = {"down": (1, 0),
              "up": (-1, 0),
              "right": (0, 1),
              "left": (0, -1)}


for row in range(ROWS):
    matrix.append(list(input()))
    if "B" in matrix[row]:
        start_row, start_col = row, matrix[row].index("B")

origin = (start_row, start_col)
matrix[start_row][start_col] = "."
outside = False
while True:
    command = input()
    curr_row, curr_col = start_row + directions[command][0], start_col + directions[command][1]

    if is_outside(curr_row, curr_col):
        print("The delivery is late. Order is canceled.")
        outside = True
        break

    if check_obstacle(curr_row, curr_col):
        continue

    if check_if_restaurant(curr_row, curr_col):
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[curr_row][curr_col] = "R"

    elif check_if_pizza_delivered(curr_row, curr_col):
        print("Pizza is delivered on time! Next order...")
        matrix[curr_row][curr_col] = "P"
        break

    else:
        matrix[curr_row][curr_col] = "."

    start_row, start_col = curr_row, curr_col

if outside:
    matrix[origin[0]][origin[1]] = " "

else:
    matrix[origin[0]][origin[1]] = "B"

print_matrix()