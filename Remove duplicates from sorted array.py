# iter through the list
# start form the second number (index 1)
# if the previous number is equal to the current:
#   remove the previous element and append nothing to the end

# edge cases:
# [1,1,1] = 1
# [1] = 1
# [0,1,2,3] = 4

def remove_duplicates(nums):
    index = 1
    list_length = len(nums)
    if list_length == 1:
        return 1
    for i in range(1, list_length):
        if nums[index] == nums[index-1]:
            del(nums[index-1])
            nums.append('')
        else:
            index += 1
    return list_length - nums.count('')

print(remove_duplicates([0,2]))
