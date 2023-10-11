import os
import re

words = []
DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
final_result = {}

with open(os.path.join(DIRECTORY_PATH, "words.txt"), "r") as word_file:
    words = word_file.read().split()

with open(os.path.join(DIRECTORY_PATH, "input.txt"), "r") as input_file:
    files = input_file.read().lower()

for word in words:
    regex = re.compile(rf"\b{word}\b")
    result = re.findall(regex, files)
    final_result[word] = len(result)

final_result = sorted(final_result.items(), key=lambda x: -x[1])


with open(os.path.join(DIRECTORY_PATH, "output.txt"), "a") as output_file:
    for el in final_result:
        word, occ = el
        output_file.write(f"{word} - {occ}\n")