a = [int(el) for el in input().split()]

try:
    index = int(input())
    print(a[index])

except ValueError as ex:
    print(f"Invalid => {ex}")

except IndexError as ex:
    print(f"Invalid => {ex}")

else:
    print("from else")

finally:
    print("from finally")
