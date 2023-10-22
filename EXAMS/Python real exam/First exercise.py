from collections import deque


fuel = [int(x) for x in input().split()]
consumtion_indexes = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])
altitude = 0

while fuel:
    curr_fuel = fuel.pop()
    curr_consumtion = consumtion_indexes.popleft()
    curr_needed_fuel = needed_fuel.popleft()

    result = curr_fuel - curr_consumtion

    if result >= curr_needed_fuel:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")

    else:
        print(f"John did not reach: Altitude {altitude+1}")
        break


if altitude > 0 and altitude < 4:
    reached = [f"Altitude {x}" for x in range(1, altitude+1)]
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached)}")

elif altitude == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

elif altitude == 4:
    print("John has reached all the altitudes and managed to reach the top!")