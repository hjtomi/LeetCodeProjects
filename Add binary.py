# decode the binaries
# add them
# code into binary
# return

def add_binary(a, b):
    int_a = int(a, 2)
    int_b = int(b, 2)
    sum_int = int_a+int_b
    sum_binary = bin(sum_int)
    return(sum_binary.removeprefix("0b"))

print(add_binary("101110111", "111101"))