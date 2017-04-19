# Interview Cake: 2nd largest element in a binary search tree
# https://www.interviewcake.com/question/python/second-largest-item-in-bst
# Miguel Aroca-Ouellette
# 01/12/2016


class BinaryTreeNode:
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

def second_largest(root):
    # Finds the second largest element in a binary search tree. O(h) time where h is the height of the tree
    if root.left is None and root.right is None:
        raise ValueError("Invalid input.")

    second = root.left
    node = root

    # Finds the rightmost node
    while node.right is not None:
        second = node
        node = node.right

    # If there's a left subtree to the rightmost node then find largest element in there, that's the second largest
    if node.left:
        node = node.left
        while node.right is not None:
            node = node.right
        second = node

    # Else the second largest is simply the parent of the rightmost node

    return second

# Test
root = BinaryTreeNode(3)
root.insert_left(2)
right = root.insert_right(4)
far_right = right.insert_right(5)
far_lr = far_right.insert_left(4.5)
far_lr.insert_right(4.6)
far_lr.insert_left(4.4)
right.insert_left(3.5)

print second_largest(root).value == 4.6
print second_largest(far_lr).value == 4.5