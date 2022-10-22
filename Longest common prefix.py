# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""

# Checks every first letter, if same checks second...

def longest_common_prefix(strs):
    prefix = ""
    if len(strs) > 0:
        shortest_word = min(strs, key=len)
        same = True

        for letter in range(len(shortest_word)):
            if not same:
                break

            for str in strs:
                if not same:
                    break
                if str[letter] != shortest_word[letter]:
                    same = False
            if same:
                prefix += shortest_word[letter]

        return prefix

    else:
        return prefix


print(longest_common_prefix(["szalma", "szabadszállás"]))
