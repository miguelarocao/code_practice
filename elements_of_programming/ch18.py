# Chapter 18 Problems

import timeit
import numpy as np
from bisect import bisect_left


# Problem 18.4
def three_sum(num, arr):
    one_arr = [False] * (num + 1)
    two_arr = [False] * (num + 1)

    for item in arr:
        one_arr[item] = True

    for i in range(num + 1):
        for step in arr:
            if i - step < 0:
                continue
            if one_arr[i - step]:
                two_arr[i] = True
                break

    for step in arr:
        if two_arr[num - step]:
            return True

    return False


def three_sum_better(num, arr):
    sum_two = []

    for first in arr:
        for second in arr:
            sum_two.append(first + second)

    sum_two.sort()

    for third in arr:
        res = binary_search(sum_two, num - third)
        if res > -1:
            return True

    return False


def three_sum_best(num, arr):
    arr.sort()

    for third in arr:
        if check_two_pair(num - third, arr):
            return True

    return False


def check_two_pair(goal, arr):
    # Returns True if pair is found
    # O(n)

    first = 0
    second = len(arr) - 1

    while first < second:
        if arr[first] + arr[second] == goal:
            return True
        elif arr[first] + arr[second] < goal:
            first += 1
        else:
            second -= 1

    return False


def test_18_4():
    arr = np.unique(np.random.randint(0, 999, 10000))
    num = 10000

    print three_sum(num, arr)
    print three_sum_better(num, arr)
    print three_sum_best(num, arr)

    input_str = str(num) + ',[' + ','.join(map(str, arr)) + ']'
    print timeit.timeit('three_sum(' + input_str + ')', setup='from __main__ import three_sum', number=10)
    # print timeit.timeit('three_sum_better(' + input_str + ')', setup='from __main__ import three_sum_better', number=10)
    print timeit.timeit('three_sum_best(' + input_str + ')', setup='from __main__ import three_sum_best', number=10)


# Binary search for use in 18.4
def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end


# Problem 18.7
def max_water(arr):
    left = best_left = 0
    right = best_right = len(arr) - 1

    best_volume = min(arr[best_left], arr[best_right]) * best_right

    while left < right:
        new_volume = min(arr[left], arr[right]) * (right - left)

        # Check greedy
        if new_volume > best_volume:
            best_volume = new_volume
            best_left, best_right = left, right

        # Check what to step
        if arr[left] > arr[right]:
            right -= 1
        elif arr[left] < arr[right]:
            left += 1
        else:
            left += 1
            right -= 1

    return best_left, best_right


def test_18_7():
    arr = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 3, 4, 1]
    arr2 = [1, 1, 1, 9, 9, 1, 1, 1]
    arr3 = [1, 2, 1, 1, 2, 1, 1, 1]

    print max_water(arr) == (4, 16)
    print max_water(arr2) == (3, 4)
    print max_water(arr3) == (0, 7)



def skyline(buildings):
    active = []
    max_rec = 0

    for i in range(len(buildings)):
        while active != [] and buildings[i] < buildings[active[-1]]:
            # Pop building and get length
            # print active
            new = active.pop()
            height = buildings[new]
            if active != []:
                width = new - active[-1]
            else:
                width = new + 1

            # print "%d %d %d" % (i, width, height)
            max_rec = max(max_rec, width * height)

        if active != [] and buildings[i] == buildings[active[-1]]:
            active[-1] = i
        else:
            active.append(i)

    # print active

    # Calculate remaining
    while active != []:
        new = active.pop()
        if active == []:
            max_rec = max(max_rec, len(buildings) * buildings[new])
        else:
            max_rec = max(max_rec, (len(buildings) - new) * buildings[new])

    return max_rec


def test_18_8():
    arr = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
    print skyline(arr) == 20

    arr = [10,8,6,4]
    print skyline(arr) == 18

    arr = [1,2,5,9]
    print skyline(arr) == 10



def main():
    # test_17_1()
    # test_17_2()

    # test_18_4()
    test_18_8()


if __name__ == '__main__':
    main()
