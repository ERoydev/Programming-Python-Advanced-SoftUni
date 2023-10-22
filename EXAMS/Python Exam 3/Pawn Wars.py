
def check_promotion(row, col, promotion_row):
    if row == promotion_row:
        return True

def increment_row_by_color(row, color):
    if color == "White":
        return row - 1

    if color == "Black":
        return row + 1

def move_pawn(row, curr_pawn):
    matrix[curr_row][curr_col] = curr_pawn

def check_if_capture(row, col, color):
    col_left = max(col - 1, 0)
    col_right = min(col + 1, 7)
    row = increment_row_by_color(row, color)
    oposite_pawn = "b" if color == "White" else "w"

    if (matrix[row][col_left] == oposite_pawn) or (matrix[row][col_right] == oposite_pawn):
        return row, matrix[row].index(oposite_pawn)

chess = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

matrix = []
for row in range(8):
    matrix.append(input().split())
    if "w" in matrix[row]:
        white_row, white_col = row, matrix[row].index("w")

    if "b" in matrix[row]:
        black_row, black_col = row, matrix[row].index("b")

turns = {
    True: {"row": white_row,"col": white_col, "color": "White", 'promotion_row': 0},
    False: {"row": black_row, "col": black_col, "color": "Black", "promotion_row": 7}
}

turn = True
while True:
    curr_row, curr_col, promotion_row, color = turns[turn]['row'], turns[turn]['col'], turns[turn]['promotion_row'], turns[turn]['color']

    if check_promotion(curr_row, curr_col, promotion_row):
        print(f"Game over! {color} pawn is promoted to a queen at {chess[curr_col]}{8 - curr_row}.")
        break

    result = check_if_capture(curr_row, curr_col, color)

    if result:
        print(f"Game over! {color} win, capture on {chess[result[1]]}{8 - result[0]}.")
        break

    curr_el = matrix[curr_row][curr_col]
    matrix[curr_row][curr_col] = "-"
    curr_row = increment_row_by_color(curr_row, color)
    turns[turn]['row'] = curr_row
    move_pawn(curr_row, curr_el)

    turn = not turn