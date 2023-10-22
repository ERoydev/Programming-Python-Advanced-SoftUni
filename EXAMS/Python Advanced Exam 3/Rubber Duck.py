from collections import deque

operations = [(0, 60), (61, 120), (121, 180), (181, 240)]

rewards = {
    (0, 60): ["Darth Vader Ducky", 0],
    (61, 120): ["Thor Ducky", 0],
    (121, 180): ["Big Blue Rubber Ducky", 0],
    (181, 240): ["Small Yellow Rubber Ducky", 0]
}


time_to_complete = deque([int(x) for x in input().split()])
tasks_number = [int(x) for x in input().split()]


while time_to_complete and tasks_number:
    time = time_to_complete.popleft()
    tasks = tasks_number.pop()

    result = time * tasks

    if result > 240:
        tasks_number.append(tasks - 2)
        time_to_complete.append(time)
        continue


    for elements in operations:
        start, end = elements

        if start <= result <= end:
            rewards[elements][1] += 1
            continue


print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in rewards.items():
    print(f"{value[0]}: {value[1]}")






