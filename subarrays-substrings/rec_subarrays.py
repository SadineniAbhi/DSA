def generate_all_substrings(string, i, j):
    if i == len(string):
        return
    if j == len(string):
        generate_all_substrings(string, i + 1, i + 1)
        return
    print(string[i:j + 1])  # Print the substring from i to j
    generate_all_substrings(string, i, j + 1)


