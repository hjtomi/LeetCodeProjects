# if the last element is smaller than 9, just add one to it and return the list
# if the last element is 9, set that to 0 and check if there is a previous element
#                                                        False: make 1
#                                                        True: if it is nine do the same, if not add 1

def plus_one(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    index = 1
    for i in range(len(digits)):
        if digits[-index] == 9:
            digits[-index] = 0
            if index == len(digits):
                digits.insert(0, 1)
        else:
            digits[-index] += 1
            break
        index += 1
    return digits


print(plus_one([2]))

