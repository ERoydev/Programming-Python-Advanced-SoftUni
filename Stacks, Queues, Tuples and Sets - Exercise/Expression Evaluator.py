from collections import deque

line = [int(x) if x.isdigit() else x for x in input().split()]
queue = deque()


for el in line:
    result = 0
    if el == "+":
        result = queue.popleft()
        while queue:
            result += queue.popleft()

        queue.append(int(result))

    elif el == "-":
        result = queue.popleft()
        while queue:
            result -= queue.popleft()

        queue.append(int(result))

    elif el == "*":
        result = queue.popleft()
        while queue:
            result *= queue.popleft()

        queue.append(int(result))

    elif el == "/":
        result = queue.popleft()
        while queue:
            result /= queue.popleft()

        queue.append(int(result))

    else:
        queue.append(int(el))

print(*queue)