def check_square(row, col, element):
    if matrix[row][col+1] != element:
        return False

    if matrix[row+1][col] != element:
        return False

    if matrix[row+1][col+1] != element:
        return False

    return True

ROWS, COLS = [int(x) for x in input().split()]
matrix = [input().split() for i in range(ROWS)]
founded = 0


for row in range(len(matrix)):
    if row == ROWS-1:
        break

    for col in range(len(matrix[row])):
        if col == COLS-1:
            continue

        if check_square(row, col, matrix[row][col]):
            founded += 1

print(founded)