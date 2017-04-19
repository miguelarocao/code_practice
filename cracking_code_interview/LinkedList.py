# Singly Linked list implementation

class Node:

    def __init__(self, data, double = False):
        self.data = data
        self.next = None
        self.double = double
        if self.double:
            self.prev = None

    def append_to_tail(self, data):

        curr_node = self
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = Node(data)

        if self.double:
            curr_node.next.prev = curr_node

        return curr_node.next

    def __str__(self):
        node = self

        output = ''
        while node is not None:
            output += str(node.data) + " -> "
            node = node.next

        output += 'End'

        return output

    @staticmethod
    def remove_next(node):
        node.next = node.next.next

def test():
    head = Node("A")
    head.append_to_tail("B")
    head.append_to_tail("C")
    head.append_to_tail("D")

    print head


if __name__ == '__main__':
    test()