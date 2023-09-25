def check_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        return True


def find_starting_positions():
    for row in range(size):
        if "B" in matrix[row]:
            return row, matrix[row].index("B")


size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]


cols, result, directions = len(matrix[0]), {}, {
    "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

bunny_row, bunny_col = find_starting_positions()


def movement():
    for direction, (row, col) in directions.items():
        bunny_move_row, bunny_move_col = bunny_row + row, bunny_col + col
        total = 0

        for jump in range(cols):
            if check_valid_index(bunny_move_row, bunny_move_col):
                result[direction] = result.get(direction, [])
                result[direction].append([bunny_move_row, bunny_move_col])
                total += matrix[bunny_move_row][bunny_move_col]

                bunny_move_row, bunny_move_col = bunny_move_row + row, bunny_move_col + col

            else:
                break
        if direction in result:
            result[direction].append(total)

movement()
sorted_result = sorted(result.items(), key=lambda x: -x[1][-1])[0]

if sorted_result:
    print(sorted_result[0])
    [print(row) for row in sorted_result[1]]