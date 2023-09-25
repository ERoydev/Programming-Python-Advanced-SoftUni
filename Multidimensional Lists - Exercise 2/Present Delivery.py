
def generous_presents_give(curr_row, curr_col, total_presents, present_given):
    for value in directions:
        curr_row += directions[value][0]
        curr_col += directions[value][1]

        if check_for_nice_kid(curr_row, curr_col):
            total_presents -= 1
            present_given += 1

        if matrix[curr_row][curr_col] == "X":
            total_presents -= 1
            matrix[curr_row][curr_col]

        matrix[curr_row][curr_col] = "-"
        if total_presents == 0:
            return total_presents, present_given

        curr_row -= directions[value][0]
        curr_col -= directions[value][1]


    return total_presents, present_given

def check_for_cookie(row, col):
    if matrix[row][col] == "C":
        return True

def check_for_nice_kid(row, col):
    if matrix[row][col] == "V":
        return True

def is_outside(row, col):
    return 0 > row or row >= SIZE or 0 > col or col >= SIZE


directions = {"left": (0, -1),
              "right": (0, 1),
              "up": (-1, 0),
              "down": (1, 0)}


total_presents = int(input())
SIZE = int(input())

matrix = []
nice_kids = 0
present_given_to_nice_kids = 0

for row in range(SIZE):
    matrix.append(input().split())

    if "S" in matrix[row]:
        santa_row, santa_col = (row, matrix[row].index("S"))

    nice_kids += matrix[row].count("V")

matrix[santa_row][santa_col] = "-"

while total_presents > 0:
    user_input = input()
    if user_input == "Christmas morning":
        break

    curr_row, curr_col = santa_row + directions[user_input][0], santa_col + directions[user_input][1]
    if is_outside(curr_row, curr_col):
        continue

    nice_kid = check_for_nice_kid(curr_row, curr_col)
    cookie_check = check_for_cookie(curr_row, curr_col)

    if cookie_check:
        total_presents, present_given_to_nice_kids = generous_presents_give(curr_row, curr_col, total_presents, present_given_to_nice_kids)

    if nice_kid:
        total_presents -= 1
        present_given_to_nice_kids += 1

    matrix[curr_row][curr_col] = "-"

    santa_row, santa_col = curr_row, curr_col


if total_presents <= 0 and nice_kids - present_given_to_nice_kids > 0:
    print("Santa ran out of presents!")

matrix[santa_row][santa_col] = "S"
[print(*row) for row in matrix]


if nice_kids > present_given_to_nice_kids:
    print(f"No presents for {nice_kids - present_given_to_nice_kids} nice kid/s.")

else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")