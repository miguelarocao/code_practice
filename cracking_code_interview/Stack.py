# Stack implementation

from LinkedList import Node

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        out = self.top
        self.top = self.top.next

        return out

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def __str__(self):
        return str(self.top)