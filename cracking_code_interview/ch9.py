# Chapter 9 Problems

import timeit
import random

# Problem 9.5
def perm_string(string, perm_dict=None, use_dp=True):
    if perm_dict is None:
        perm_dict = {}

    if string == '':
        return ['']

    output = []
    for i in range(len(string)):
        sub_str = string[:i] + string[i + 1:]

        if sub_str not in perm_dict or not use_dp:
            perm_dict[sub_str] = perm_string(sub_str, perm_dict=perm_dict)

        output += [string[i] + sub_perm for sub_perm in perm_dict[sub_str]]

    return output


def perm_string_v2(string):
    # Better implementation
    if string == '':
        return ['']
    elif len(string) == 1:
        return [string]

    sub_perm = perm_string_v2(string[1:])

    output = []
    for sub_str in sub_perm:
        for i in range(len(sub_str) + 1):
            output.append(sub_str[:i] + string[0] + sub_str[i:])

    return output


def combo_change(n, denoms=None):
    # Denominations left to go through
    # Goes back to front
    if denoms is None:
        denoms = [1, 5, 10, 25]

    # Check if base case
    if n == 0 or len(denoms) == 1:
        return 1

    # Reduce denomination if necessary
    while denoms[-1] > n:
        denoms.pop()

    # Compute
    run_sum = 0
    for i in range(n / denoms[-1] + 1):
        # print "n=%d, denom=%d, calling n=%d, denom=%d result %d" %(n, denoms[-1], n-i*denoms[-1],denoms[-2],
        #                                                            combo_change(n - i * denoms[-1], denoms[:-1]))
        run_sum += combo_change(n - i * denoms[-1], denoms[:-1])

    return run_sum


class Box:
    instance_count = 0
    def __init__(self, w, d, h):
        self.w = w
        self.d = d
        self.h = h
        self.id = Box.instance_count
        Box.instance_count += 1

    def larger_than(self, box):
        assert isinstance(box, Box)

        if box.w < self.w and box.d < self.d and box.h < self.h:
            return True
        return False

    def smaller_than(self, box):
        assert isinstance(box, Box)

        if box.w > self.w and box.d > self.d and box.h > self.h:
            return True
        return False


def stack_boxes(boxes, box_mem=None):

    # NOTE: Could pass "base box" through and use that as DP key, doesn't get used, but would avoid us having
    # to generate a unique hashmap key for each set of boxes, since that set is simply based on the base box anyways

    # For dynamic programming
    if box_mem is None:
        box_mem = {}

    # Base case
    box_str = boxes_to_str(boxes)
    if len(boxes) == 1:
        return boxes[0].h
    elif box_str in box_mem:
        return box_mem[box_str]

    # List of flags: if True then there does not exist a larger box, if False then there does, if None then unknown
    base_flag = [None] * len(boxes)

    # Smaller flags: True if already marked as smaller in the current collection of boxes
    small_flag = [False] * len(boxes)

    highest = 0
    base_idx = 0
    compare_idx = base_idx + 1
    curr_list = []
    length = len(boxes)

    while base_idx < length:
        # If not already compared and isn't a base box
        if not small_flag[compare_idx] and not base_flag[compare_idx]:
            if boxes[base_idx].larger_than(boxes[compare_idx]):
                # Box is smaller than base box

                # Marked as smaller in case base changes
                small_flag[compare_idx] = True
                curr_list.append(compare_idx)

                # Not a base box
                base_flag[compare_idx] = False


            elif boxes[base_idx].smaller_than(boxes[compare_idx]):
                # Box is larger than base box

                # add old box to list, new base box
                base_flag[base_idx] = False
                small_flag[base_idx] = True
                curr_list.append(base_idx)

                # Swap
                base_idx = compare_idx

                # Reset comparison
                compare_idx = 0

        compare_idx += 1
        if compare_idx == length:
            # Call recursion on base box
            height = boxes[base_idx].h+ stack_boxes([boxes[idx] for idx in curr_list], box_mem=box_mem)
            box_mem[boxes_to_str([boxes[base_idx]] + [boxes[idx] for idx in curr_list])] = height
            if height > highest:
                highest = height

            # Reset smaller flags
            small_flag = [False] * len(boxes)

            # Set base as checked
            base_flag[base_idx] = True

            # Get next potential base
            base_idx = get_next_potential_base(base_flag)

            # Reset comparison
            compare_idx = 0

    return highest

def get_next_potential_base(base_flag):
    # Get next potential base
    i = 0
    length = len(base_flag)
    while i < length:
        if base_flag[i] is None:
            break
        i += 1

    return i

def boxes_to_str(boxes):
    # Converts a list of boxes to a unique string.
    # Order is not important, always yields the same string within a python call (uses Box instance count)

    sorted_list = sorted(boxes, key=lambda x: x.id)

    return ','.join([str(box.id) for box in sorted_list])


test_str = 'acbasbdadda'

if __name__ == '__main__':
    boxes = [Box(4,4,6), Box(4,6,4), Box(3,5,3), Box(3,3,5), Box(1,4,2), Box(2,2,3), Box(1.5, 1.5, 1.5)]

    random.shuffle(boxes)
    print stack_boxes(boxes)
    #print stack_boxes(boxes)
# print timeit.timeit("perm_string(test_str)", 'from __main__ import perm_string, test_str',number = 10)
# print timeit.timeit("perm_string(test_str, use_dp = False)", 'from __main__ import perm_string, test_str', number=10)
# print timeit.timeit("perm_string_v2(test_str)", 'from __main__ import perm_string_v2, test_str', number=10)
