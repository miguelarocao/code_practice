# Interview Cake: Superbalanced Binary Trees
# https://www.interviewcake.com/question/python/balanced-binary-tree
# Miguel Aroca-Ouellette
# 06/17/2016


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

    def is_leaf(self):
        if (self.left is None) and (self.right is None):
            return True
        return False

    # Written
    def check_super(self):
        ''' Checks if tree extending from current node is superbalanced. '''
        min_depth = 1e20
        max_depth = 0

        print '\t'.join(map(str, ["Value", "Depth", "Maximum", "Minimum"]))

        curr_depth = 0
        stack = []
        if self.left:
            stack.append([self.left, curr_depth + 1])
        if self.right:
            stack.append([self.right, curr_depth + 1])
        while stack:
            # go to next node
            curr_node, curr_depth = stack.pop()

            print '\t\t'.join(map(str, [curr_node.value, curr_depth, max_depth, min_depth]))

            # check for violations of superbalanced
            if curr_depth > (min_depth + 1):
                print "False: Current depth is much deeper than min."
                return False

            # add children to stack if they exist
            if curr_node.left:
                stack.append([curr_node.left, curr_depth + 1])
            if curr_node.right:
                stack.append([curr_node.right, curr_depth + 1])

            # check depth
            if curr_node.is_leaf():
                if curr_depth < min_depth:
                    min_depth = curr_depth
                if curr_depth > max_depth:
                    max_depth = curr_depth

                # check for violation
                if min_depth < (max_depth - 1):
                    print "False: Minimum is much shallower than max."
                    return False

        return True


def main():

    mytree = BinaryTreeNode(0)

    # Test tree, Toggle Node 14 to create super or non-superbalanced tree
    mytree.insert_left(1)
    mytree.insert_right(2)
    mytree.left.insert_left(3)
    mytree.left.insert_right(4)
    mytree.right.insert_left(5)
    mytree.right.insert_right(6)
    mytree.left.left.insert_left(7)
    mytree.left.left.insert_right(8)
    mytree.left.right.insert_right(9)
    mytree.right.right.insert_left(10)
    mytree.right.right.insert_right(11)
    mytree.left.left.left.insert_left(12)
    mytree.left.left.left.insert_right(13)
    mytree.right.left.insert_right(14)
    print mytree.check_super()

if __name__ == '__main__':
    main()
