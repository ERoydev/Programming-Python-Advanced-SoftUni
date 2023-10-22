# Input
initial_fuel = list(map(int, input().split()))
consumption_indexes = list(map(int, input().split()))
needed_fuel = list(map(int, input().split()))

altitudes_reached = []

for altitude in needed_fuel:
    current_fuel = initial_fuel[-1]
    consumption_index = consumption_indexes[0]
    initial_fuel.pop()
    consumption_indexes.pop(0)

    if current_fuel - consumption_index >= altitude:
        altitudes_reached.append(altitude)
        print(f"John has reached: Altitude {altitude}")
    else:
        break

if not altitudes_reached:
    print("John did not reach any altitude.")
else:
    print("John failed to reach the top.")
    print("Reached altitudes:", end=' ')
    print(", ".join([f"Altitude {altitude}" for altitude in altitudes_reached]))

if not needed_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
