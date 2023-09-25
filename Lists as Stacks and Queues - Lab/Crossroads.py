from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
crashed = False
passed = 0

while not crashed:
    user_input = input()
    if user_input == "END":
        break

    elif user_input == "green":
        green_light = green_light_duration
        total_time = green_light + free_window_duration

        while cars:
            if green_light < 1:
                break
            car = cars.popleft()

            if len(car) > total_time:
                print("A crash happened!")
                print(f"{car} was hit at {car[total_time]}.")
                crashed = True
                break

            green_light -= len(car)
            total_time -= len(car)
            passed += 1

    else:
        cars.append(user_input)


if not crashed:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")

