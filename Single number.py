def single_number(nums):
    res = 0
    for n in nums:
        res^=n
        print(n)
    return res

print("\n", single_number([1,1,2,3,4,4,3]))
