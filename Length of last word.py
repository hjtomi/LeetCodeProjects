# cut the string into a list with all the words
# check the length of the -1st element in the list

def length_of_last_word(s):
    word_list = s.split(" ")
    print(word_list)
    index = 1
    for i, word in enumerate(word_list):
        if "" != word_list[-index]:
            return len(word_list[-index])
        index += 1


print(length_of_last_word("alma"))
