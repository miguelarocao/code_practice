# Chapter 13

import os
import sys
import timeit

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path + '/../cracking_code_interview/')

from cracking_code_interview.BinaryTree import BinaryNode

# Problem 13.1
def palin_perm(str):
    str = str.lower()
    char_count = {}
    odd_count = 0

    for c in str:
        if c not in char_count:
            char_count[c] = 0
            
        char_count[c] += 1
        if char_count[c] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1

    return (odd_count == 1 or odd_count == 0)

def palin_perm_test():
    test_str = {'level': True, 'foobaraboof': True, 'edified': True, 'test': False, 'a': True, 'abacbb': False}

    for str, expected in test_str.iteritems():
        if palin_perm(str) != expected:
            print "Failure on " + str
            return

    print "Success!"

# Problem 13.3
def nearest_rep(arr_str):
    closest_pair = None
    str_hash = {}

    for i in range(len(arr_str)):
        if arr_str[i] in str_hash:
            # We've seen the word before
            dist = i - str_hash[arr_str[i]]
            if closest_pair is None or dist < closest_pair:
                closest_pair = dist
        str_hash[arr_str[i]] = i

    return closest_pair

# Problem 13.4
def LCA_close(node1, node2):
    # Note: modifies the inputs
    hashmap = set()

    while True:
        for node in (node1, node2):
            if node in hashmap:
                return node
            hashmap.add(node)
        if node1.parent is not None:
            node1 = node1.parent
        if node2.parent is not None:
            node2 = node2.parent

        if node1.parent is None and node2.parent is None:
            return None

def test_13_4():
    # Runs test
    #    3
    #  1   5
    # 0 2 4 6
    #        7

    root = BinaryNode(3, True)
    right = root.add_right(5)
    left = root.add_left(1)
    deep_right = right.add_right(6)
    deep7 = deep_right.add_right(7)
    deep4 = right.add_left(4)
    left.add_left(0)
    left.add_right(2)

    print LCA_close(deep4, deep7) == right

# Problem 13.7
def smallest_covering_sub(arr, str_set):

    # Step 1: Build a hashtable of the word positions
    cache = {}
    for i, word in enumerate(arr):
        if word in cache:
            cache[word].append(i)
        else:
            cache[word] = [i]

    # Step 2: Find the most restrictive word
    restr_word = min([(len(cache[word]), word) for word in str_set], key = lambda x: x[0])[1]

    # Step 3: Find the smallest covering set using greedy ranges
    greedy_range = (float("-inf"), float("inf"))
    for pos in cache[restr_word]:
        curr_range = (pos, pos)
        for word in str_set - {restr_word}:
            greedy_idx = None
            greedy_close = None
            for idx in cache[word]:
                range_d = dist_range(idx, curr_range)
                if range_d == 0:
                    # In range, thus break
                    greedy_idx = idx
                    break
                elif greedy_idx is None or range_d < greedy_close:
                    greedy_idx = idx
                    greedy_close = range_d

            if not (curr_range[0] <= greedy_idx <= curr_range[1]):
                curr_range = (min(curr_range[0], greedy_idx), max(curr_range[1], greedy_idx))

        if abs(curr_range[0] - curr_range[1]) < abs(greedy_range[0] - greedy_range[1]):
            greedy_range = curr_range

    return greedy_range

def dist_range(num, num_range):
    # Finds the smallest distance between a number and a range
    # If the number is within the range (inclusive) it returns 0
    # i.e. dist_range(8, (3, 6)) = 2
    assert(isinstance(num_range, tuple))

    if num_range[0] <= num <= num_range[1]:
        return 0
    else:
        return min(abs(num - num_range[0]), abs(num - num_range[1]))

def smallest_covering_sub_book(arr, str_set):
    # The idea is to crawl through arr, and check the str_set using a hash.
    # THIS IS WRONG, need to keep COUNT of keywords. Function 'smallest_sub()' is the correct implementation.

    hmap = {}
    for string in str_set:
        hmap[string] = False # True denotes that its currently in the range

    best_range = (float("-inf"), float("inf"))

    match_count = 0
    left = 0
    for right, word in enumerate(arr):

        # If in str_set and not currently in our range then increment match_count
        if word in hmap and not hmap[word]:
            hmap[word] = True
            match_count += 1

        # If all words found, decrease size until not all words found
        while match_count == len(str_set):
            if (right - left) < (best_range[1] - best_range[0]):
                best_range = (left, right)

            # Reduce size by removing word
            if arr[left] in hmap and hmap[arr[left]]:
                hmap[arr[left]] = False
                match_count -= 1
            left += 1

    return best_range

def smallest_sub(arr, keywords):
    # Second attempt without looking at first attempt

    # handle unreasonable input
    if len(keywords) == 0:
        return 0

    best_cover = None
    front = back = 0
    covered = {}
    while True:
        # Crawl front
        while len(covered) < len(keywords):
            if front >= len (arr):
                return best_cover
            word = arr[front]
            if word in keywords:
                if word in covered:
                    covered[word] += 1
                else:
                    covered[word] = 1
            front += 1

        # Crawl back
        while len(covered) == len(keywords):
            word = arr[back]
            if word in keywords:
                covered[word] -= 1
                if covered[word] == 0:
                    covered.pop(word)
            back += 1

        if best_cover is None or (front - back) < (best_cover[1] - best_cover[0]):
            best_cover = (back - 1, front - 1)

def test_13_7():
    text = "My paramount object in this struggle is to save is Union and not either to save or to destroy slavery"
    keywords = {"save", "Union", "is"}
    text = "apple banana apple apple dog cat apple dog banana apple cat dog"
    keywords = {'banana', 'cat'}
    arr = text.split(' ')

    print smallest_covering_sub(arr, keywords)
    print smallest_covering_sub_book(arr, keywords)
    print smallest_sub(arr, keywords)

    input_arr = str(arr)
    input_set = str(keywords)

    print timeit.timeit(setup = 'from __main__ import smallest_covering_sub;', stmt='smallest_covering_sub(%s, %s)' % (input_arr, input_set), number = 10)
    print timeit.timeit(setup = 'from __main__ import smallest_covering_sub_book;', stmt='smallest_covering_sub_book(%s, %s)' % (input_arr, input_set), number = 10)

def nearest_rep_test():
    arr = "All work and no play makes for no work no fun and no results".split(' ')

    print nearest_rep(arr)

# Problem 13.10

def longest_contained_interval(arr):

    hmap = {i for i in arr}

    greedy_size = 0
    while len(hmap) > 0:
        num = hmap.pop()
        left = right = num
        left -= 1
        right += 1
        while left in hmap:
            hmap.remove(left)
            left -= 1
        while right in hmap:
            hmap.remove(right)
            right += 1

        if right - left - 1 > greedy_size:
            greedy_size = right - left - 1

    return greedy_size

def test_13_10():
    arr = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]

    print longest_contained_interval(arr) == 6

def main():
    # palin_perm_test()
    # test_13_4()
    # test_13_7()
    test_13_10()

if __name__ == '__main__':
    main()