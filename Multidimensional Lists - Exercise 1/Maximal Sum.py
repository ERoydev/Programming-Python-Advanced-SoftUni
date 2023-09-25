def is_outside(n, side):
    return n + 2 >= side

def check_3x3_square(row, col):
    element = 0
    square = []
    idx = -1

    for i in range(row, row+step):
        idx += 1
        square.append([])

        for j in range(col, col + step):
            element += matrix[i][j]
            square[idx].append(matrix[i][j])

    return element,square

ROWS, COLS = [int(x) for x in input().split()]

matrix = []
step = 3
max_sum = float('-inf')
square_max_sum = []

for row in range(ROWS):
    row_element = [int(x) for x in input().split()]
    matrix.append(row_element)


for row in range(len(matrix)):
    if is_outside(row, ROWS):
        break

    for col in range(len(matrix[row])):
        if is_outside(col, COLS):
            continue

        element, square_matrix = check_3x3_square(row, col)
        if element > max_sum:
            max_sum = element
            square_max_sum = square_matrix

print(f"Sum = {max_sum}")
[print(*el) for el in square_max_sum]