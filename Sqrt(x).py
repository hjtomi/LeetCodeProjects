# compute the square root of x
# store it in a variable
# convert to a string
# split at dot
# return the first
import math


def my_sqrt(x):
    root = str(math.sqrt(x))
    if "." in root:
        temp = root.partition(".")
        return temp[0]
    else:
        return root


print(my_sqrt(4))