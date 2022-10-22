def search_insert(nums, target):
    # these vars are the range of the possible numbers
    lo, hi = 0, len(nums) - 1

    # if lo is smaller than hi it's good, if it's equal there is only 1 number left, but if it's higher we need to stop
    while lo <= hi:
        # mid is the index of the middle number of the current possible numbers
        mid = (lo + hi) // 2
        mid_number = nums[mid]

        if mid_number == target:
            return mid
        if mid_number > target:
            hi = mid - 1
        if mid_number < target:
            lo = mid + 1
    try:
        if hi - lo < 1:
            if nums[lo] > target:
                return lo
            if nums[hi] < target:
                return hi + 1
            else:
                return hi
    except IndexError:
        return hi+1

print(search_insert([1,3,4,6,8], 9))