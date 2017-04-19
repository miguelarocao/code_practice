# Chapter 12 Problems

import random as rnd
import math
import timeit

# Problem 12.1
def find_first(arr, goal):
    left = 0
    right = len(arr) - 1
    last_seen = None
    while left <= right:
        mid = (left + right) / 2

        if arr[mid] == goal:
            last_seen = mid

        if goal <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return last_seen


def test_12_1():
    arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 400]

    print find_first(arr, 108)

# Problem 12.8
def find_k_largest(arr, k):
    left = 0
    right = len(arr) - 1
    while True:
        pivot = rnd.randint(left, right)
        #print pivot
        # print arr[pivot]
        # print arr[left:right + 1]
        new_pivot_idx = partition(arr, left, right, pivot)

        #print new_pivot_idx
        # print arr[left:right + 1]

        if new_pivot_idx == len(arr) - k:
            return arr[new_pivot_idx]
        elif new_pivot_idx < (len(arr) - k):
            left = new_pivot_idx + 1
        else:
            right = new_pivot_idx - 1
            #k = k - (len(arr) - new_pivot_idx)

def test_12_8():
    arr = [3,2,1,5,4]
    rnd.seed(12345)
    print find_k_largest(arr, 3)

def partition(arr, left, right, pivot):
    # Pivot is the index of the pivot
    # Returns new index of pivot
    # No duplicates
    # NOTE: Could just pivot to the end and then swap into the correct place instead of using a tracker

    new_pivot_idx = right
    pivot_val = arr[pivot]
    pivot_tracker = pivot

    i = left
    while True:
        if arr[i] > pivot_val:
            arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
            if arr[i] == pivot_val:
                pivot_tracker = i
            new_pivot_idx -= 1
        else:
            i += 1

        if i > new_pivot_idx:
            break

    arr[new_pivot_idx], arr[pivot_tracker] = arr[pivot_tracker], arr[new_pivot_idx]
    return new_pivot_idx

# Problem 12.5
def real_root(num, thresh):
    assert(thresh != 0)

    powten = 10**(int(math.log(num, 10)))
    output = 0
    while True:
        bot = 0
        top = 10
        while bot <= top:
            mid = (bot + top)/2
            mid_num = output + mid*powten
            if mid_num**2 <= num:
                bot = mid + 1
            else:
                top = mid - 1

        digit = bot - 1
        output += digit*powten
        powten /= 10.0

        # print output

        if abs(output**2 - num) <= thresh:
            break

    return output

def real_root_book(num, thresh):

    if num < 1.0:
        left = num
        right = 1
    else:
        left = 1
        right = num

    while abs(left - right) > thresh:
        mid = (left + right)/2.0

        if mid**2 > num:
            right = mid
        else:
            left = mid

    return left

def test_12_5():
    print timeit.timeit('real_root(n, 0.00001)', setup = 'import random; from __main__ import real_root; n =random.uniform(0,1000);',number=10000)
    print timeit.timeit('real_root_book(n, 0.00001)', setup='import random; from __main__ import real_root_book; n =random.uniform(0,1000);', number=10000)
    print real_root(2, 0.000001)
    print real_root_book(2, 0.000001)

def search_2d(matrix, goal):
    r = len(matrix) - 1
    c = 0
    while r >= 0 and c < len(matrix[0]):
        if matrix[r][c] > goal:
            r -= 1
        elif matrix[r][c] < goal:
            c += 1
        else:
            return True

    return False

def test_12_6():
    matrix = [[-1,2,4,4,16], [1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]

    print search_2d(matrix, 7)
    print search_2d(matrix, 8)
    print search_2d(matrix, 0)

def main():
    # test_12_1()
    # test_12_5()
    test_12_6()


if __name__ == '__main__':
    main()
