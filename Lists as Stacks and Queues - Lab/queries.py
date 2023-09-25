
stack = []

n = int(input())

def check_stack_size():
    if len(stack) != 0:
        return True

for i in range(n):
    num = input()

    if num.startswith("1"):
        _, number = num.split()
        stack.append(int(number))

    elif check_stack_size():
        if num.startswith("2"):
            if stack:
                stack.pop()

        elif num.startswith("3"):
            print(max(stack))

        elif num.startswith("4"):
            print(min(stack))


print(", ".join(str(stack.pop()) for _ in range(len(stack))))
