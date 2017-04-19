# Chapter 16 Problems

# Problem 16.11
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value, weight):
        self.children.append((TreeNode(value), weight))
        return self.children[-1][0]

    def get_children(self):
        return self.children

def get_diameter(root):
    # Returns (Longest Path in Subtree, Furthest Node from Root)
    # Base case -> No chlidren
    if root.children == []:
        return (0, 0)

    # Otherwise compare longest path in subtrees to longest path through root
    greedy_diam = 0
    max_data = [0]*2
    for child, edge_weight in root.get_children():
        diameter, max_dist = get_diameter(child)
        if diameter > greedy_diam:
            greedy_diam = diameter
        update_top_two(max_data, max_dist + edge_weight)

    # Longest path comparison
    comp_diam = sum(max_data)
    if comp_diam > greedy_diam:
        greedy_diam = comp_diam

    return greedy_diam, max_data[0]

def update_top_two(arr, new):
    # Largest at front of arr

    if new > arr[0]:
        arr[1] = arr[0]
        arr[0] = new
    elif new > arr[1]:
        arr[1] = new


def test_16_11():
    root = TreeNode(0)
    left = root.add_child(1, 7)
    mid = root.add_child(2, 14)
    right = root.add_child(3, 3)
    deep_left = left.add_child(4, 4)
    left.add_child(5, 3)
    right.add_child(6, 2)
    deep_right = right.add_child(7, 1)
    deep_left.add_child(8, 6)
    deep_right.add_child(9, 6)
    deeper_right = deep_right.add_child(10, 4)
    deeper_right.add_child(11, 4)
    deepest_right = deeper_right.add_child(12, 2)
    deepest_right.add_child(13, 1)
    deepest_right.add_child(14, 2)
    deepest_right.add_child(15, 3)

    print get_diameter(root)

def main():
    test_16_11()

if __name__ == '__main__':
    main()