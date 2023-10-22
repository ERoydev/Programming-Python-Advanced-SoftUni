from collections import deque

words = {
    'rose': set(),
    'tulip': set(),
    'lotus': set(),
    'daffodil': set()
}

vowels = deque(input().split())
consonants = input().split()
founded = False

while vowels and consonants:
    if founded:
        break
    curr_vow = vowels.popleft()
    curr_cons = consonants.pop()

    for word in words.keys():
        if curr_vow in word:
            words[word].add(curr_vow)

        if curr_cons in word:
            words[word].add(curr_cons)

        if len(words[word]) == len(set(x for x in word)):
            print(f"Word found: {word}")
            founded = True
            break

if not founded:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
