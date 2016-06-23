# Interview Cake: Valid Binary Search Tree
# https://www.interviewcake.com/question/python/bst-checker?utm_source=weekly_email
# Miguel Aroca-Ouellette
# 06/18/2016


class BinaryTreeNode:

    # Provided
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    # Written
    def check_bin_search(self):
        """ Checks if the tree extending from the current node is a valid binary search tree."""

        min_range = -1e20    # node value must be greater than this
        max_range = 1e20     # node value must be less than this

        stack = []
        if self.left:
            stack.append([self.left, min_range, self.value])
        if self.right:
            stack.append([self.right, self.value, max_range])

        while stack:
            curr_node, min_range, max_range = stack.pop()
            if curr_node.value < min_range or curr_node.value > max_range:
                print "Found invalid node: " + str(curr_node.value)
                return False

            if curr_node.left:
                stack.append([curr_node.left, min_range, curr_node.value])

            if curr_node.right:
                stack.append([curr_node.right, curr_node.value, max_range])

        return True


def main():

    # Test tree. Toggle node 60/40 to create an invalid/valid binary search tree.
    mytree = BinaryTreeNode(50)
    mytree.insert_left(30)
    mytree.insert_right(80)
    mytree.left.insert_left(20)
    mytree.left.insert_right(60) #40
    mytree.right.insert_left(70)
    mytree.right.insert_right(90)

    print mytree.check_bin_search()

main()
