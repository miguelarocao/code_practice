# Chapter 6 Problems

import random


# Problem 6.11
# Improvement on problem: This handles n x m arrays!
def random_subset(arr, size):
    for i in range(size):
        idx = random.randint(i, len(arr) - 1)
        arr[i], arr[idx] = arr[idx], arr[i]


def test_6_11():
    arr = range(1, 8)
    size = 4
    random_subset(arr, size)
    print arr[:size]


# Problem 6.17
def spiral_ord(arr):
    output = [None] * len(arr[0]) * len(arr)
    lb = ub = idx = 0
    rb = len(arr[0]) - 1
    db = len(arr) - 1

    while idx < len(output):
        for i in range(lb, rb):
            output[idx] = arr[ub][i]
            idx += 1

        for i in range(ub, db):
            output[idx] = arr[i][rb]
            idx += 1

        for i in range(rb, lb, -1):
            output[idx] = arr[db][i]
            idx += 1

        for i in range(db, ub, - 1):
            output[idx] = arr[i][lb]
            idx += 1

        lb += 1
        rb -= 1
        ub += 1
        db -= 1

        if idx == len(output) - 1 and rb==lb and ub == db:
            # Add central element
            output[idx] = arr[ub][rb]
            idx += 1

    return output

def test_6_17():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    print spiral_ord(arr) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    arr = [[1,2,3],[4,5,6],[7,8,9]]

    print spiral_ord(arr)


def main():
    # test_6_11()
    test_6_17()

if __name__ == '__main__':
    main()
