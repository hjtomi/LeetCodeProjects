def length_of_longest_substring(s: str) -> int:
    current_substring = ""
    longest_substring_len = 0
    starting_index = 0

    i = 0
    for _ in range(len(s)):
        if s[i] not in current_substring:
            current_substring += s[i]
            i += 1
        else:
            if len(current_substring) > longest_substring_len:
                longest_substring_len = len(current_substring)


    if len(current_substring) > longest_substring_len:
        longest_substring_len = len(current_substring)

    return longest_substring_len


print(length_of_longest_substring("dvdf"))

