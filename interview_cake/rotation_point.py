# Interview Cake: Find Rotation Point
# https://www.interviewcake.com/question/python/find-rotation-point
# Miguel Aroca-Ouellette
# 06/04/2017

"""
Key point: Huge list (need to be efficient)

If we step through the list (length n) and compare every word then we have ~2n comparisons (since every
word is compared with its 2 neighbours. If each word is at most length (m) then worst case
complexity is O(nm).

But list is sorted! Let's take advantage of that. We can do a modified binary search to find rotation
point. This would lead to an O(m*logn) solution.
How this works: Pick the middle word and compare it to the endpoints. If the left endpoint is smaller
(in alphabetical ordering) then search right subarray, otherwise search left. Repeat on recursively
smaller subarrays. Stop when midpoint is smaller than midpoint - 1, this is your rotation point.

"""

def find_rotation_point(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)/2
        if arr[mid] < arr[mid - 1]: # Because it wraps around if mid == 0 (beautiful)
            return mid

        if arr[left] > arr[mid]:
            right = mid - 1
        elif arr[right] < arr[mid]:
            left = mid + 1
        else:
            # In sorted order
            return left

# Test
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    ]

print find_rotation_point(words) == 5
print find_rotation_point(['c', 'a']) == 1
print find_rotation_point(['z']) == 0