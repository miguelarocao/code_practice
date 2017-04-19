# Chapter 10 Problems

from cracking_code_interview.BinaryTree import BinaryNode
from cracking_code_interview.Stack import Stack

def is_symmetric(root):
    left_stack = Stack()
    right_stack = Stack()
    left_stack.push(root.left)
    right_stack.push(root.right)

    while left_stack.peek() or right_stack.peek():
        left = left_stack.pop().data
        right = right_stack.pop().data

        if (left is None and right) or (left and right is None) or left.data != right.data:
            return False

        if left.data:
            # Build left stack
            left_stack.push(left.left)
            left_stack.push(left.right)

            # Build right stack
            right_stack.push(right.right)
            right_stack.push(right.left)

    return True

def is_symmetric_test():
    # Symmetric Tree
    sym_root = BinaryNode(4)
    right = sym_root.add_right(6)
    left = sym_root.add_left(6)
    left.add_right(2).add_right(3)
    right.add_left(2).add_left(3)

    # Asymmetric Tree
    asym_root = BinaryNode(4)
    right = asym_root.add_right(6)
    left = asym_root.add_left(6)
    left.add_right(5).add_right(3)
    right.add_left(2).add_left(3)

    # Asymmetric Tree b/c of uneven depth
    asym_root2 = BinaryNode(4)
    right = asym_root2.add_right(6)
    left = asym_root2.add_left(6)
    left.add_right(2).add_right(3)
    right.add_left(2)

    print is_symmetric(sym_root)
    print is_symmetric(asym_root)
    print is_symmetric(asym_root2)

# Problem 10.4
def find_LCA(node1, node2):
    # Pass 1, find depth
    depths = [0] * 2
    curr_nodes = [node1, node2]

    print "Finding depths..."

    done = [False, False]
    while True:
        for i in range(len(curr_nodes)):
            if done[i]:
                continue
            curr_nodes[i] = curr_nodes[i].parent
            depths[i] += 1

            if curr_nodes[i].parent is None:
                done[i] = True

        if all(done):
            break

    print "Finding LCA using depths..."

    # Pass 2, find LCA
    # (1) Get to same depth
    deep_node, shallow_node, depth, goal_depth = (node1, node2, depths[0], depths[1]) if depths[0] > depths[1] else (
        node2, node1, depths[1], depths[0])
    while depth != goal_depth:
        deep_node = deep_node.parent
        depth -= 1

    # (2) Find LCA
    LCA = None
    curr_nodes = [deep_node, shallow_node]
    while curr_nodes[0] is not None and curr_nodes[1] is not None:
        if curr_nodes[0] == curr_nodes[1]:
            LCA = curr_nodes[0]
            break

        for i in range(len(curr_nodes)):
            curr_nodes[i] = curr_nodes[i].parent

    return LCA


def find_LCA_test():
    # Runs test
    #    1
    #  3   2
    # 4 5 6 7
    #        8


    root = BinaryNode(1, True)
    right = root.add_right(2)
    left = root.add_left(3)
    deep_right = right.add_right(7)
    deep_right.add_right(8)
    right.add_left(6)
    left.add_left(4)
    left.add_right(5)

    print find_LCA(right.left, deep_right.right)

# Problem 10.11
def inorder_lowmem(root):
    node = root
    prev_node = root.parent # should be None

    while node is not None:
        new_prev = node
        if prev_node == node.parent:
            if node.left:
                node = node.left
            elif node.right:
                print node.data
                node = node.right
            else:
                print node.data
                node = node.parent
        elif prev_node == node.left:
            print node.data
            if node.right:
                node = node.right
            else:
                node = node.parent
        else:
            node = node.parent

        prev_node = new_prev

    return

def test_10_11():
    # Runs test
    #    3
    #  1   5
    # 0 2 4 6
    #        7

    root = BinaryNode(3, True)
    right = root.add_right(5)
    left = root.add_left(1)
    deep_right = right.add_right(6)
    deep_right.add_right(7)
    right.add_left(4)
    left.add_left(0)
    left.add_right(2)

    print "Should print out numbers in increasing order."
    inorder_lowmem(root)

# Problem 10.12
def reconstruct_handler(pre_arr, in_arr):
    # Build hashtable for in_arr indices
    inord_hash = {}
    for i, c in enumerate(in_arr):
        inord_hash[c] = i

    return reconstruct(pre_arr, in_arr, 0, len(pre_arr), 0, len(in_arr), inord_hash)


def reconstruct(pre_arr, in_arr, pre_start, pre_end, in_start, in_end, inord_hash):
    # Input check
    if (pre_end - pre_start) != (in_end - in_start):
        raise ValueError("Inputs must have equal length!")

    # Base cases
    # Empty
    if pre_end == pre_start:
        return None
    # If identical then either (A) only one node left or (B) the remaining tree is a right child only tree
    root = BinaryNode(pre_arr[pre_start])
    if pre_arr[pre_start:pre_end] == in_arr[in_start:in_end]:
        node = root
        for i in range(pre_start + 1, pre_end):
            node.right = BinaryNode(pre_arr[i])
            node = node.right
        return root

    # Else continue recursion
    idx = inord_hash[root.data]
    rel_idx = idx - in_start
    # print "Found %s at %d" % (root.data, idx)
    # print "Left inputs %d %d %d %d" % (pre_start + 1, pre_start + rel_idx + 1, in_start,  idx)
    root.left = reconstruct(pre_arr, in_arr, pre_start + 1, pre_start + rel_idx + 1, in_start,  idx, inord_hash)
    # print "Right inputs %d %d %d %d" % (pre_start + rel_idx + 1, pre_end, rel_idx + 1, in_end)
    root.right = reconstruct(pre_arr, in_arr, pre_start + rel_idx + 1, pre_end, idx + 1, in_end, inord_hash)

    return root

def test_10_12():
    pre_order = "HBFEACDGI"
    in_order =  "FBAEHCDIG"

    root = reconstruct_handler(pre_order, in_order)

    root.print_sub()


def main():
    # is_symmetric_test()
    # test_10_11()
    test_10_12()

if __name__ == '__main__':
    main()