# Interview Cake: Find A Duplicate, Space Edition
# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space
# Miguel Aroca-Ouellette
# 21/03/2017

# Iteratively shrinks the interval to check by 2
# Somewhat similar to a binary search.
# O(1) space and O(nlogn) time
#   -> O(nlogn) because do logn passes over the array
# Doesn't destroy input!
def find_duplicate_better(arr):
    # Finds a duplicate item in the input array
    # Optimized for space

    min_num = 1
    max_num = len(arr) - 1

    while min_num < max_num:
        count = 0
        mid = (min_num + max_num)/2
        # do a pass
        for val in arr:
            if min_num <= val <= mid:
                count += 1

        # check how to update range
        if count <= (mid- min_num + 1):
            min_num = mid + 1
        else:
            max_num = mid

    return min_num

# Test
input = [1,2,3,4,5,6,7,8,9,9]
print find_duplicate_better(input)