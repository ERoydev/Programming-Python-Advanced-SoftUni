from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]

challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool, current_substance = tools.popleft(), substances.pop()
    curr_result = current_tool * current_substance

    if curr_result in challenges:
        element = [el for el in range(len(challenges)) if curr_result == challenges[el]][0]
        challenges.pop(element)

    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

print(f"Tools: {', '.join(str(x) for x in tools)}") if tools else None
print(f"Substances: {', '.join(str(x) for x in substances)}") if substances else None
print(f"Challenges: {', '.join(str(x) for x in challenges)}") if challenges else None