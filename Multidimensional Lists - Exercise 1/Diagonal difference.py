
n = int(input())
matrix = []

primary_diagonal = 0
secondary_diagonal = 0

for row in range(n):
    row_element = [int(x) for x in input().split()]
    matrix.append(row_element)

    primary_diagonal += matrix[row][row]
    secondary_diagonal += matrix[row][n - row - 1]

print(abs(primary_diagonal - secondary_diagonal))
