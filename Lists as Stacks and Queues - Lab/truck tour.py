
n = int(input())
stops = 0
total_fuel = 0

for i in range(n):
    fuel, distance = [int(x) for x in input().split()]
    total_fuel += fuel

    if total_fuel >= distance:
        total_fuel -= distance

    else:
        stops += 1
        total_fuel = 0

print(stops)

