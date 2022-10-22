def two_sum(num_list, target):
    for i in range(0, len(num_list)):
        for num in range(i+1, len(num_list)):
            if num_list[i] + num_list[num] == target:
                return [i, num]


print(two_sum([2,7,11,15], 9))