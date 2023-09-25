def print_matrix(matrix):
    [print(*row) for row in matrix]

def create_matrix(matrix):
    for row in range(ROWS):
        element = input().split()
        matrix.append([int(x) if x.isdigit() else x for x in element])

    return matrix

def check_valid_coordinates(row, col):
    return (row >= 0 and row < ROWS) and (col >= 0 and col < COLS)

ROWS, COLS = [int(x) for x in input().split()]
matrix = create_matrix([])

while True:
    user_input = input()
    if user_input == "END":
        break

    args = [int(x) if x.isdigit() else x for x in user_input.split()]


    if len(args) != 5 or args[0] != "swap":
        print("Invalid input!")
        continue

    if not check_valid_coordinates(args[1], args[2]) or not check_valid_coordinates(args[3], args[4]):
        print("Invalid input!")
        continue

    matrix[args[1]][args[2]], matrix[args[3]][args[4]] = matrix[args[3]][args[4]], matrix[args[1]][args[2]]
    print_matrix(matrix)


