
seq1 = set(int(x) for x in input().split())
seq2 = set(int(x) for x in input().split())

n = int(input())

for i in range(n):
    user_input = input().split()
    command = " ".join(user_input[:2])
    numbers = set(int(x) for x in user_input[2:])

    if command == "Add First":
        seq1 = seq1.union(numbers)

    elif command == "Add Second":
        seq2 = seq2.union(numbers)

    elif command == "Remove First":
        seq1 = seq1.difference(numbers)

    elif command == "Remove Second":
        seq2 = seq2.difference(numbers)

    elif command == "Check Subset":
        print(seq1.issubset(seq2) or seq2.issubset(seq1))


print(', '.join(str(x) for x in (sorted(seq1))))
print(', '.join(str(x) for x in (sorted(seq2))))