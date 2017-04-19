# Chapter 2 problems

from LinkedList import Node


# 2.1
def remove_duplicates(head):
    seen = {head.data}
    curr_node = head
    while curr_node is not None and curr_node.next is not None:
        if curr_node.next.data in seen:
            Node.remove_next(curr_node)
        else:
            seen.add(curr_node.next.data)
        curr_node = curr_node.next

    return

# 2.3
def remove_middle(node):
    curr_node = node
    while True:
        curr_node.data = curr_node.next.data
        if curr_node.next.next is None:
            curr_node.next = None
            break
        curr_node = curr_node.next

# 2.4
def partition(head, x):
    less_start, less_end = None, None
    more_start, more_end = None, None
    curr_node = head

    while curr_node is not None:
        next = curr_node.next
        curr_node.next = None
        if curr_node.data >= x:
            if more_start:
                more_end.next = curr_node
                more_end = curr_node
            else:
                more_start = curr_node
                more_end = curr_node
        else:
            if less_start:
                less_end.next = curr_node
                less_end = curr_node
            else:
                less_start = curr_node
                less_end = curr_node
        curr_node = next

    less_end.next = more_start
    return less_start

# Problem 2.5
def add_linkedlists(head1, head2):
    curr1 = head1
    curr2 = head2
    carry = 0
    result_start = None
    result_curr = None

    while True:
        d1 = d2 = 0

        if curr1:
            d1 = curr1.data
            curr1 = curr1.next
        if curr2:
            d2 = curr2.data
            curr2 = curr2.next

        new_num = d1 + d2 + carry
        new_data = new_num % 10
        carry = new_num / 10
        if result_start:
            result_curr.next = Node(new_data)
            result_curr = result_curr.next
        else:
            result_start = Node(new_data)
            result_curr = result_start

        if curr1 is None and curr2 is None:
            break

    return result_start

head = Node(12)
head.append_to_tail(1)
head.append_to_tail(2)
head.append_to_tail(11)
head.append_to_tail(3)

print head

#remove_duplicates(head)
# remove_middle(head.next.next)
# head = partition(head, 6)

num1 = Node(7)
num1.append_to_tail(1)
num1.append_to_tail(6)

num2 = Node(5)
num2.append_to_tail(9)
num2.append_to_tail(2)

head = add_linkedlists(num1, num2)

print head