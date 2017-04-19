# Chapter 15 Problems

import sys
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path + '/../cracking_code_interview/')

from cracking_code_interview.BinaryTree import BinaryNode

# Problem 15.1
def check_bst_rec(root):
    # Recursive call
    if root is None:
        return None, None, True

    lmin, lmax, lr = check_bst_rec(root.left)
    rmin, rmax, rr = check_bst_rec(root.right)

    result = (lmax is None or lmax <= root.data) and (rmin is None or root.data <= rmin) and lr and rr

    if lmin is None:
        lmin = root.data
    if rmax is None:
        rmax = root.data

    return lmin, rmax, result

def check_bst(root):
    _, _, result = check_bst_rec(root)
    return result

def check_bst_test():
    root = BinaryNode(19)
    left = root.add_left(7)
    right = root.add_right(43)
    left_left = left.add_left(3)
    left_right = left.add_right(11)
    left_left.add_left(2)
    left_left.add_right(5)
    lrr = left_right.add_right(17)
    lrr.add_left(13)
    right_left = right.add_left(23)
    rlr = right_left.add_right(37)
    rlr.add_right(41)
    rlr.add_left(29).add_right(31)
    brk_node = right.add_right(47).add_right(53)

    print "Success" if check_bst(root) == True else "Failure :("

    brk_node.add_left(100)

    print "Success" if check_bst(root) == False else "Failure :("

    root = BinaryNode(19)
    root.add_left(7).add_right(20)
    root.add_right(43)

    print "Success" if check_bst(root) == False else "Failure :("

# Problem 15.2
def bst_greater(bst, value):
    # assume bst points to root

    curr_node = bst
    smallest_greater = None

    while curr_node is not None:
        if value < curr_node.data:
            smallest_greater = curr_node.data
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    return smallest_greater


def bst_greater_test():
    # Build BST on p.251

    root = BinaryNode(19)
    left = root.add_left(7)
    right = root.add_right(43)
    left_left = left.add_left(3)
    left_right = left.add_right(11)
    left_left.add_left(2)
    left_left.add_right(5)
    lrr = left_right.add_right(17)
    lrr.add_left(13)
    right_left = right.add_left(23)
    rlr = right_left.add_right(37)
    rlr.add_right(41)
    rlr.add_left(29).add_right(31)
    right.add_right(47).add_right(53)

    print bst_greater(root, 52)


# Problem 15.3
def bts_k_largest(bts, k):
    if bts is None:
        return "Empty binary tree!"

    right_result = []
    left_result = []
    mid_result = []
    if bts.right is not None:
        right_result = bts_k_largest(bts.right, k)
    if len(right_result) < k:
        mid_result = [bts.data]
    if bts.left is not None and len(right_result) < (k - 1):
        left_result = bts_k_largest(bts.left, k - len(right_result) - 1)

    # print right_result

    return right_result + mid_result + left_result


def bts_k_largest_test():
    root = BinaryNode(19)
    left = root.add_left(7)
    right = root.add_right(43)
    left_left = left.add_left(3)
    left_right = left.add_right(11)
    left_left.add_left(2)
    left_left.add_right(5)
    lrr = left_right.add_right(17)
    lrr.add_left(13)
    right_left = right.add_left(23)
    rlr = right_left.add_right(37)
    rlr.add_right(41)
    rlr.add_left(29).add_right(31)
    right.add_right(47).add_right(53)

    print bts_k_largest(root, 10)


# Problem 15.4
def bst_LCA(root, n1, n2):
    # Input is BST with DISTINCT node values (data)
    # Returns None if n1 or n2 is not in the BST
    #   -> Not necessary for the problem, this makes it slower but the complexity is the same
    if root is None:
        return None

    cn = root
    while cn is not None:
        if n1.data < cn.data < n2.data or n2.data < cn.data < n1.data:
            if in_bst(cn, n1) and in_bst(cn, n2):
                break
            return None
        elif cn.data == n1.data:
            if in_bst(n1, n2):
                break
            return None
        elif cn.data == n2.data:
            if in_bst(n2, n1):
                break
            return None
        else:
            if n1.data > cn.data:
                cn = cn.right
            else:
                cn = cn.left

    return cn

def in_bst(root, node):
    # Returns true if the node is in the BST, otherwise False
    cn = root
    while cn is not None:
        if cn == node:
            return True
        if node.data >= cn.data:
            cn = cn.right
        else:
            cn = cn.left

    return False

def test_15_4():
    root = BinaryNode(19)
    left = root.add_left(7)
    right = root.add_right(43)
    left_left = left.add_left(3)
    left_right = left.add_right(11)
    left_left.add_left(2)
    left_left.add_right(5)
    lrr = left_right.add_right(17)
    lrr.add_left(13)
    right_left = right.add_left(23)
    rlr = right_left.add_right(37)
    rlr.add_right(41)
    rlr.add_left(29).add_right(31)
    right.add_right(47).add_right(53)

    print bst_LCA(root, left_left, lrr).data

# Problem 15.5
def build_BST(pre, max_value = float("inf"), curr_idx = None):

    curr_idx = curr_idx if curr_idx else 0

    # Base case
    if curr_idx >= len(pre) or pre[curr_idx] >= max_value:
        return None, curr_idx

    root = BinaryNode(pre[curr_idx])
    root.left, curr_idx = build_BST(pre, pre[curr_idx], curr_idx + 1)
    root.right, _ = build_BST(pre, max_value, curr_idx)

    return root, curr_idx

def test_15_5():
    pre = [2,1,4,3]

    root = build_BST(pre)[0]

    print root
    print root.left
    print root.right

def main():
    # check_bst_test()
    # test_15_4()
    test_15_5()

if __name__ == '__main__':
    main()