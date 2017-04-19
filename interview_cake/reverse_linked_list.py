# Interview Cake: Reverse Linked List
# https://www.interviewcake.com/question/python/reverse-linked-list
# Miguel Aroca-Ouellette
# 19/04/2017

# Linked List Node Class (Provided)
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        curr_node = self
        output = ''
        while curr_node is not None:
            output += str(curr_node.value) + ' -> '
            curr_node = curr_node.next

        return output[:-4]

# Note: Must do it in place

# O(n) time and O(1) space
def reverse(head):
    # Reverse the input linked list
    curr_node = head
    prev_node = None

    while curr_node is not None:
        # Save next
        next_node = curr_node.next

        # Point backwards
        curr_node.next = prev_node

        # Move forward through list
        prev_node = curr_node
        curr_node = next_node

    return prev_node

# Example List
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
print head
print reverse(head)

# Edge cases
edge_1 = LinkedListNode(1)
print edge_1
print reverse(edge_1)

edge_0 = None
print edge_0
print reverse(edge_0)