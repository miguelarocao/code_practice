# Interview Cake: Find A Duplicate, Space Edition BEAST MODE
# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space-beast-mode
# Miguel Aroca-Ouellette
# 28/03/2017

def find_duplicate(arr):
    # Finds a duplicate in input array, optimized for space

    # Start at end
    fast = slow = len(arr) - 1

    # Step until cycle is found
    while True:
        fast = arr[arr[fast] - 1] - 1
        slow = arr[slow] - 1

        if fast == slow:
            break

    # Restart the slow pointer and store previous as you go
    slow = len(arr) - 1

    while slow != fast:
        slow = arr[slow] - 1
        fast = arr[fast] - 1

    return slow + 1

# Test
arr = [1,2,3,3,4,5,6,7]
print find_duplicate(arr)