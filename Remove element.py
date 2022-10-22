# edge cases:
# [3,5,12] 5 = 2
# [0] 0 = 0

# iter though the elements
# if current equals the val:
#   remove it and don't increment index and put '' at the end
#

def remove_element(nums, val):
    index = 0
    for num in nums:
        if nums[index] == val:
            del(nums[index])
            nums.append('')
        else:
            index += 1
    return len(nums) - nums.count('')

print(remove_element([0], 0))