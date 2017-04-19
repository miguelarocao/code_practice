# Interview Cake: Merge Sorted Arrays
# https://www.interviewcake.com/question/python/merge-sorted-arrays
# Miguel Aroca-Ouellette
# 22/11/2016


def merge_sorted(arr1, arr2):
    # Merges two sorted arrays. O(n) time and space

    new_arr = [None] * (len(arr1) + len(arr2))

    i = 0
    j = 0
    while True:
        if arr1[i] < arr2[j]:
            new_arr[i + j] = arr1[i]
            i += 1
        else:
            new_arr[i + j] = arr2[j]
            j += 1

        if i >= len(arr1):
            # Copy over rest of 2
            new_arr[i + j:] = arr2[j:]
            break
        elif j >= len(arr2):
            # Copy over rest of arr1
            new_arr[i + j:] = arr1[i:]
            break

    return new_arr

# Test`
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_sorted(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]