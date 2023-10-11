

file = open("numbers.txt", "r")
result = [i.strip() for i in file]

print(sum(int(i) for i in result))