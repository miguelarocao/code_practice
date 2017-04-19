# Chapter 8 Problems

from cracking_code_interview.LinkedList import Node

# Problem 8.3
def test_cycle(start):
    fp = sp = start
    while True:
        if fp.next is None or fp.next.next is None:
            return None
        fp = fp.next.next
        sp = sp.next

        if fp == sp:
            break

    fp = start
    while fp != sp:
        fp = fp.next
        sp = sp.next

    return sp

def test_8_3():
    # No cycle
    start = Node(0)

    print test_cycle(start) is None

    # Cycle
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    start.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    print test_cycle(start) == n2

# Problem 8.4
def test_overlap(start1, start2):
    node1, node2 = start1, start2

    while True:
        if node1 == node2:
            return True
        elif node1.next is None and node2.next is None:
            break

        if node1.next is not None:
            node1 = node1.next

        if node2.next is not None:
            node2 = node2.next

    return False

def test_8_4():
    # Do not overlap
    start1 = Node(0)
    start1.append_to_tail(1).append_to_tail(2)
    start2 = Node(0)
    start2.append_to_tail(1).append_to_tail(2).append_to_tail(3)

    print test_overlap(start1, start2) == False

    # Do overlap
    start1 = Node(0)

    print test_overlap(start1, start1) == True

    start1 = Node(0)
    next11 = Node(1)
    next12 = Node(2)
    next13 = Node(3)
    start1.next = next11
    next11.next = next12
    next12.next = next13

    start2 = Node(0)
    next21 = Node(1)
    start2.next = next21
    next21.next = next13

    next13.append_to_tail(4).append_to_tail(5)

    print test_overlap(start1, start2) == True

# Problem 8.10
def even_odd_merge(start):
    even_end = even_start = start
    odd_end = odd_start = start.next
    count = 2
    node = odd_start.next if odd_start is not None else None
    while node is not None:
        if count%2 == 0:
            even_end.next = node
            even_end = node
        else:
            odd_end.next = node
            odd_end = node

        count += 1
        node = node.next

    # Make sure odd_end points to nothing
    odd_end.next = None

    # Even end points to start
    even_end.next = odd_start

    return even_start

def test_8_10():

    # Generate list
    n = 19
    start = Node(0)
    node = start
    for i in range(1, n):
        node.next = Node(i)
        node = node.next

    print start

    print even_odd_merge(start)

def main():
    # test_8_3()
    # test_8_4()
    test_8_10()

if __name__ == '__main__':
    main()