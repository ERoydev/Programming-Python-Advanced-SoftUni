def is_dead(row,col):
    return matrix[row][col] <= 0

def is_outside(row, col):
    return row < 0 or row >= n or col < 0 or col >= n

def explode_all_squares(squares, explosion_damage):
    for row, col in squares:
        if is_outside(row, col) or is_dead(row, col):
            continue

        matrix[row][col] -= explosion_damage

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

coordinates = input().split()

for coordinate in coordinates:
    row, col = [int(x) for x in coordinate.split(",")]

    if is_dead(row, col):
        continue

    explosion_damage, matrix[row][col] = matrix[row][col], 0

    explosion_squares = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col -1), (row, col + 1), (row+1, col-1), (row +1, col), (row +1, col + 1)]
    explode_all_squares(explosion_squares, explosion_damage)

alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
[print(*row) for row in matrix]
