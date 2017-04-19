# Chapter 14 Problems

import os
import sys

dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_path + '/../cracking_code_interview/')

from cracking_code_interview.LinkedList import Node


# Problem 14.4
class CalEvent():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return self.name


def biggest_overlap_cal(cal):
    by_start = sorted(cal, key=lambda x: x.start)
    by_end = sorted(cal, key=lambda x: x.end)

    start_idx = 0  # ITEM TO ADD
    end_idx = 0  # ITEM PART OF GROUP
    overlap_size = 0
    greedy_max = 0

    while start_idx < len(cal):
        if by_start[start_idx].start < by_end[end_idx].end:
            overlap_size += 1
            start_idx += 1
        else:
            overlap_size -= 1
            end_idx += 1

        if overlap_size > greedy_max:
            greedy_max = overlap_size

    return greedy_max


def test_14_4():
    events = [CalEvent("E1", 1, 5), CalEvent("E2", 6, 10), CalEvent("E3", 11, 13), CalEvent("E4", 14, 15),
              CalEvent("E5", 2, 7), CalEvent("E6", 8, 9), CalEvent("E7", 12, 15), CalEvent("E8", 4, 5),
              CalEvent("E9", 9, 17)]

    print biggest_overlap_cal(events)


# Problem 14.5
def merging_intervals(initial, new):
    # Step through and create new interval set

    output = []
    i = 0
    # Push smaller
    while i < len(initial) and initial[i][1] < new[0]:
        output.append(initial[i])
        i += 1

    # Combine while in range
    output.append(new)
    while i < len(initial):
        if initial[i][0] > output[-1][1]:
            break
        output[-1][0] = min(output[-1][0], initial[i][0])
        output[-1][1] = max(output[-1][1], initial[i][1])
        i += 1

    output.extend(initial[i:])

    print output
    return output


def test_14_5():
    initial = [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]
    new = [1,8]

    print merging_intervals(initial, new) == [[-4, -1], [0, 9], [11, 12], [14, 17]]
    print merging_intervals(initial, [-5, 18]) == [[-5, 18]]
    print merging_intervals(initial, [-6, -5]) == [[-6,-5], [-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]
    print merging_intervals(initial, [20,21]) == [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17], [20,21]]
    print merging_intervals(initial, [12,13]) == [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 13], [14, 17]]



# Problem 14.6
class Endpoint:
    def __init__(self, time, end_type):
        assert (end_type in ["open", "closed", 'o', 'c'])

        self.time = time
        self.end_type = end_type
        if self.end_type == 'o':
            self.end_type = 'open'
        elif self.end_type == 'c':
            self.end_type = 'closed'

    def __cmp__(self, other):
        # Only good for the sorting
        if self.time == other.time:
            if self.end_type != other.end_type:
                if self.end_type == "closed":
                    return -1
                else:
                    return 1

        return cmp(self.time, other.time)

    def __str__(self):
        return "%s%d" % ("o" if self.end_type == "open" else "c", self.time)


class Interval:
    def __init__(self, start, end):
        assert (isinstance(start, Endpoint))
        assert (isinstance(end, Endpoint))

        self.start = start
        self.end = end

    def __str__(self):
        return "(%s, %s)" % (str(self.start), str(self.end))


# Not super great code, but it works. HAVE TO BE CAREFUL WHEN COMPARING ENDPOINTS
def union_intervals(intervals):
    intervals.sort(key=lambda x: x.start)  # sort by start

    union = [intervals[0]]

    for inter in intervals:
        # if inter.end.time == 17:
        #     print union[-1]
        #     print union[-1].end
        if inter.start.time < union[-1].end.time or (
                        inter.start.time == union[-1].end.time and (inter.start.end_type != union[-1].end.end_type or
                                                                        (inter.start.end_type == union[
                                                                            -1].end.end_type and inter.start.end_type == 'closed'))):
            # Then replace

            # If falls completely within the old interval -> do nothing
            if inter.end.time < union[-1].end.time:
                pass
            elif inter.end.time == union[-1].end.time:  # equal time
                if inter.end.end_type == 'closed':
                    union[-1].end.end_type = 'closed'  # close it
                    # if its open you do nothing since c + o = c, o + o = o -> identity!
            else:
                # Otherwise replace the end
                union[-1].end = inter.end
        else:
            # print "Append"
            union.append(inter)

    return union


def test_14_6():
    # First set - should be separate
    intervals = [Interval(Endpoint(0, "open"), Endpoint(5, "open")),
                 Interval(Endpoint(5, "open"), Endpoint(10, "closed"))]
    print map(str, union_intervals(intervals))

    # Second set - should be together
    intervals = [Interval(Endpoint(0, "open"), Endpoint(5, "open")),
                 Interval(Endpoint(5, "closed"), Endpoint(10, "closed"))]
    print map(str, union_intervals(intervals))

    # Third set
    intervals = [Interval(Endpoint(0, 'o'), Endpoint(3, 'o')), Interval(Endpoint(1, 'c'), Endpoint(1, 'c')),
                 Interval(Endpoint(2, 'c'), Endpoint(4, 'c')), Interval(Endpoint(3, 'c'), Endpoint(4, 'o')),
                 Interval(Endpoint(5, 'c'), Endpoint(7, 'o')), Interval(Endpoint(7, 'c'), Endpoint(8, 'o')),
                 Interval(Endpoint(8, 'c'), Endpoint(11, 'o')), Interval(Endpoint(9, 'o'), Endpoint(11, 'c')),
                 Interval(Endpoint(12, 'c'), Endpoint(14, 'c')), Interval(Endpoint(12, 'o'), Endpoint(16, 'c')),
                 Interval(Endpoint(13, 'o'), Endpoint(15, 'o')), Interval(Endpoint(16, 'o'), Endpoint(17, 'o'))]

    print map(str, union_intervals(intervals))


# Problem 14.9
def sort_list(head, length=None):
    # Uses merge sort. Stable!
    # sorts in INCREASING order.

    if length is None:
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1

    # Base case
    if length == 2:
        if head.data <= head.next.data:
            return head
        else:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head
    elif length == 1:
        head.next = None
        return head

    # Otherwise sort both "halves"
    print "L " + str(length / 2)
    node = head
    for _ in range(length / 2):
        node = node.next
    l_head = sort_list(head, length / 2)

    print "R " + str(length - length / 2)
    r_head = sort_list(node, length - length / 2)

    # Merge sorted halves
    l_node = l_head
    r_node = r_head
    head = node = None
    while l_node is not None and r_node is not None:
        if l_node.data <= r_node.data:
            if head is None:
                head = node = l_node
            else:
                node.next = l_node
                node = node.next
            l_node = l_node.next
        else:
            if head is None:
                head = node = r_node
            else:
                node.next = r_node
                node = node.next
            r_node = r_node.next

    # Only one of the following two for loops happens
    while l_node is not None:
        node.next = l_node
        node = node.next
        l_node = l_node.next

    while r_node is not None:
        node.next = r_node
        node = node.next
        r_node = r_node.next

    return head


def test_14_9():
    head = Node(3)
    head.append_to_tail(2)
    head.append_to_tail(1)

    new_head = sort_list(head)
    print new_head

def compute_cap(input_salaries, target):
    run_sum = 0
    salaries = sorted(input_salaries)
    for i in range(len(salaries)):
        if run_sum + salaries[i]*(len(salaries) - i) >= target:
            break
        run_sum += salaries[i]

    return (target - run_sum)/(len(salaries) - i)

def test_14_10():
    salaries = [90,30,100,40,20]
    target = 210
    print compute_cap(salaries, target)

def main():
    # test_14_5()
    # test_14_4()
    # test_14_6()
    # test_14_9()
    test_14_10()


if __name__ == '__main__':
    main()
