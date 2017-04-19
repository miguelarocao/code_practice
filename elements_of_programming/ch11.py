# Chapter 11 Problems

import heapq as hq
import math
import numpy as np


# Problem 11.1
def merge_sorted(arrs):
    heap = []
    for i in range(len(arrs)):
        hq.heappush(heap, (arrs[i][0], i))

    arr_points = [1] * len(arrs)
    output = []
    while heap != []:
        # Get smallest item
        item, arr_idx = hq.heappop(heap)
        output.append(item)

        # Push new item to heap if possible
        if arr_points[arr_idx] < len(arrs[arr_idx]):
            hq.heappush(heap, (arrs[arr_idx][arr_points[arr_idx]], arr_idx))

            # Increase indices
            arr_points[arr_idx] += 1

    return output


def test_11_1():
    arrs = [[3, 5, 7], [0, 6], [0, 6, 28], [0, 6, 10]]

    print merge_sorted(arrs)

# Problem 11.2
def sort_inc_dec(arr):
    inc_idxs = [0]
    arrs = []
    for i in range(1, len(arr)):
        if len(inc_idxs)%2 == 1 and arr[i] < arr[i - 1]:
            arrs.append(arr[inc_idxs[-1]:i])
            inc_idxs.append(i)
        elif len(inc_idxs)%2 == 0 and arr[i] > arr[i - 1]:
            arrs.append(arr[i - 1: inc_idxs[-1] - 1: - 1])
            inc_idxs.append(i)

    # Check last section and flip if necessary
    if arr[-1] < arr[-2]:
        arrs.append(arr[: inc_idxs[-1] - 1: - 1])

    return merge_sorted(arrs)

def test_11_2():
    arr = [5,6,9,8,2,3,4,5,2,0]
    print sort_inc_dec(arr)
    print sorted(arr)

# Problem 11.4
def k_closest_stars(stars, k):
    heap = []
    for star in stars[:k]:
        hq.heappush(heap, (-star_dist(star), star))

    for star in stars[k:]:
        if -star_dist(star) > heap[0][0]:
            hq.heappop(heap)
            hq.heappush(heap, (-star_dist(star), star))

    output = []
    for _ in range(k):
        output.insert(0, (hq.heappop(heap)[1]))

    return output


def test_11_4():
    stars = []
    for i in range(10):
        stars.append(tuple(np.random.randint(0, 1000, 3)))

    print sorted(stars, key=lambda x: star_dist(x))[:5]
    print k_closest_stars(stars, 5)


def star_dist(coords):
    return math.sqrt(math.pow(coords[0], 2) + math.pow(coords[1], 2) + math.pow(coords[2], 2))


# Problem 11.6
def k_largest_maxheap(maxheap, k):
    heap = [(-maxheap[0], 0)]
    output = [None] * k
    for i in range(k):
        val, idx = hq.heappop(heap)
        output[i] = -val

        # Push children
        for child_idx in 2 * idx + 1, 2 * idx + 2:
            if child_idx >= len(maxheap):
                continue
            hq.heappush(heap, (-maxheap[child_idx], child_idx))

    return output


def test_11_6():
    arr = [561, 314, 401, 28, 156, 359, 271, 11, 3]
    print sorted(arr, reverse=True)[:5]
    print k_largest_maxheap(arr, 5)


def main():
    # test_11_1()
    # test_11_4()
    # test_11_6()
    test_11_2()

if __name__ == '__main__':
    main()
