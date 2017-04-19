# Queue implementation

from LinkedList import Node

class Queue:
    #FILO

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        if self.first is None:
            self.first = self.last = Node(data)
        else:
            new_node = Node(data)
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            raise ValueError("Queue is empty!")

        out = self.first
        self.first = self.first.next

        return out

    def is_empty(self):
        if self.first is None:
            return True
        return False

    def __str__(self):
        curr_node = self.first
        out = "[Front] "
        while curr_node is not None:
            out += str(curr_node.data) + " "
            curr_node = curr_node.next

        out += "[End]"

        return out


if __name__ == '__main__':
    q = Queue()

    print q

    q.enqueue(1)

    print q

    q.enqueue(2)

    print q

    q.enqueue(3)

    print q

    q.dequeue()

    print q

    q.dequeue()

    print q

    q.dequeue()

    print q