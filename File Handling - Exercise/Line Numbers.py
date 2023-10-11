def find_counters_in_lines_and_return_final_product(lines):
    final = ""
    for idx, line in enumerate(lines):
        punctuation_count, word_count = 0, 0
        for el in line:
            if el in "?!.,'-":
                punctuation_count += 1

            if el.isalpha():
                word_count += 1

        final += f"Line {idx+1}: {line.strip()} ({word_count})({punctuation_count})\n"
    return final


with open("text.txt", "r") as file, open("output.txt", "w") as output_file:
    all_lines = file.readlines()

    output_file.write(find_counters_in_lines_and_return_final_product(all_lines))


