from collections import deque

ROWS, COLS = [int(x) for x in input().split()]
text = deque([x for x in input()])


matrix = []


for row in range(ROWS):
    matrix.append(deque())


    for col in range(COLS):
        element = text.popleft()
        text.append(element)

        if row % 2 == 0:
            matrix[row].append(element)

        else:
            matrix[row].appendleft(element)


for row in matrix:
    print(''.join(row))