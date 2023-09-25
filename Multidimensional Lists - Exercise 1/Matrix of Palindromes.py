
ROWS, COLS = [int(x) for x in input().split()]

matrix = []
base = 97

for row in range(ROWS):
    matrix.append([])
    for col in range(COLS):
        row_element = chr(base + row)
        col_element = chr(base + row + col)

        matrix[row].append(row_element + col_element + row_element)

[print(*row) for row in matrix]
