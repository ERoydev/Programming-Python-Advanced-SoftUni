
def negative_vs_positive(numbers):
    positive = sum(list(filter(lambda x: x > 0, numbers)))
    negative = sum(list(filter(lambda x: x < 0, numbers)))

    print(negative)
    print(positive)

    if abs(negative) > positive:
        return "The negatives are stronger than the positives"

    return "The positives are stronger than the negatives"

seq = [int(x) for x in input().split()]
print(negative_vs_positive(seq))