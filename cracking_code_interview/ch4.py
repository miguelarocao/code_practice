import numpy as np
from BinaryTree import BinaryNode

# Problem 4.1
def is_balanced(root):

    if root == None:
        return True, 0

    bal_r, height_r = is_balanced(root.right)
    bal_l, height_l = is_balanced(root.left)

    balanced = (abs(height_l - height_r) <= 1) and bal_r and bal_l

    return balanced, max(height_r, height_l) + 1

# Problem 4.3
def ordered_to_search_tree(arr):
    assert isinstance(arr, list)

    # Get middle
    mid = len(arr)/2

    # Create nodes
    node =  BinaryNode(arr[mid])
    if arr[mid + 1:] != []:
        node.add_right(ordered_to_search_tree(arr[mid + 1:]))
    if arr[:mid] != []:
        node.add_left(ordered_to_search_tree(arr[:mid]))

    return node

def find_first_ancestor(root, first_goal, second_goal, top = True):
    # Finds the first common ancestor of the two goal nodes

    curr_find = [None] * 3

    if root == first_goal:
        curr_find[0] = first_goal
    if root == second_goal:
        curr_find[1] = second_goal
    if root is None:
        return None, None, None

    for node in (root.left, root.right):
        first, second, ancestor = find_first_ancestor(node, first_goal, second_goal, top = False)

        if ancestor:
            return ancestor if top else (None, None, ancestor)

        if first:
            curr_find[0] = first
        if second:
            curr_find[1] = second

        if curr_find[0] and curr_find[1]:
            return root if top else (None, None, root)

    # print "%s: %s %s %s" % tuple(map(lambda x: str(x.data) if x else "None", (root, first_r, second_r, ancestor)))

    if top:
        return None
    return tuple(curr_find)


def main():
    # ======== Balanced test =======
    #    1
    #  3   2
    # 4 5 6 7
    #        8
    #
    root = BinaryNode(1)
    right = root.add_right(2)
    left = root.add_left(3)
    deep_right = right.add_right(7)
    deep_right.add_right(8)
    right.add_left(6)
    left.add_left(4)
    left.add_right(5)
    # print is_balanced(root)

    # ======== Ordered Binary Tree Test =======
    # np.random.seed(12345)
    # arr = list(np.unique(np.random.randint(0, 100, size = np.random.randint(4, 10))))
    # arr.sort()
    #
    # print arr
    # root = ordered_to_search_tree(arr)
    # print root

    # ======== First Common Ancestor test=======

    ancestor = find_first_ancestor(root, deep_right.right, deep_right.right)
    if ancestor:
        print ancestor.data
    else:
        print "No ancestor:("

    return

if __name__ == '__main__':
    main()
