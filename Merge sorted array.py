# iter through nums2
# iter thought nums1 from the start
# when the first bigger number is encountered, insert it before that bigger number and set a variable to the bigger
#                                                                                              numbers position + 1
# iter thought nums1 form the variable set previously


def merge(nums1, m, nums2, n):
    for i, num2 in enumerate(nums2):
        index = 0
        for _ in range(index, len(nums1)):
            if index == len(nums1)-n:
                nums1.insert(index+i, num2)
                index += 1
                nums1.pop()
                break
            if nums1[index] > num2:
                nums1.insert(index, num2)
                index += 1
                nums1.pop()
                break
            index += 1
    return nums1


print(merge([0], 0, [1], 1))
