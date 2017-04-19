# Chapter 9 Problems

from cracking_code_interview.BinaryTree import BinaryNode
from cracking_code_interview.Queue import Queue
from cracking_code_interview.Stack import Stack

# Problem 9.2

def eval_RPN(rpn_str):
    stack = Stack()
    arr = rpn_str.split(',')
    i = 0

    while i < len(arr):

        while not is_op_RPN(arr[i]):
            stack.push(arr[i])
            i += 1

        # print stack
        # evaluate
        B = stack.pop().data
        A = stack.pop().data
        stack.push(base_eval_RPN(A, B, arr[i]))
        i += 1

    return stack.pop().data

def is_op_RPN(str):
    return str in ['+','-','x','/']

def base_eval_RPN(A, B, op):
    # print "%s %s %s" % (A, B, op)
    if op == '+':
        return str(int(A) + int(B))
    elif op == '-':
        return str(int(A) - int(B))
    elif op == 'x':
        return str(int(A)*int(B))
    elif op == '/':
        return str(int(A)/int(B))
    else:
        raise ValueError("Invalid operator!")

def eval_RPN_test():
    test1 = "3,4,+"
    test2 = "3,4,+,2,x"
    test3 = "3,4,+,2,x,1,+"
    test4 = "3,4,+,1,+,7,8,+,-9,+,x"
    test5 = "-120,4,/"

    print "Test 1: Expected: 7, Got: %s " % (eval_RPN(test1))
    print "Test 2: Expected: 14, Got: %s " % (eval_RPN(test2))
    print "Test 3: Expected: 15, Got: %s " % (eval_RPN(test3))
    print "Test 4: Expected: 48, Got: %s " % (eval_RPN(test4))
    print "Test 5: Expected: -30, Got: %s " % (eval_RPN(test5))


# Problem 9.7

def bintree_arr(root):
    curr_depth = 0
    q = Queue()
    q.enqueue((root, curr_depth))
    output =[[]]

    while not q.is_empty():
        node, depth = q.dequeue().data

        if depth != curr_depth:
            output.append([])

        curr_depth = depth
        output[-1].append(node.data)

        if node.left is not None:
            q.enqueue((node.left, depth + 1))
        if node.right is not None:
            q.enqueue((node.right, depth + 1))

    return output

def bintree_arr_test():
    # Define a binary tree of the form
    #    1
    #  3   2
    # 4 5 6 7
    #        8

    root = BinaryNode(1, True)
    right = root.add_right(2)
    left = root.add_left(3)
    deep_right = right.add_right(7)
    deep_right.add_right(8)
    right.add_left(6)
    left.add_left(4)
    left.add_right(5)

    print "Expected: [[1], [3, 2], [4, 5, 6, 7], [8]"
    print "Actual: ",
    print bintree_arr(root)


# Problem 9.8
class CircularQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.front = 0
        self.back = -1 # Points where last item is
        self.num_elem = 0

    def enqueue(self, item):
        self.num_elem += 1
        if self.num_elem > len(self.arr):
            self._resize()
        self.back = self.inc_idx(self.back)

        self.arr[self.back] = item

    def dequeue(self):
        if self.num_elem == 0:
            print "Empty Queue!"
            return None

        self.num_elem -= 1
        self.front = self.inc_idx(self.front)

        return self.arr[self.front - 1]

    def inc_idx(self, idx):
        idx += 1
        if idx == len(self.arr):
            idx = 0
        return idx

    def __len__(self):
        return self.num_elem

    def _resize(self):
        # Doubles Size
        if self.front <= self.back:
            # Increase size at back
            # print "INCREASE AT BACK"
            self.arr = self.arr + [None] * len(self.arr)

        else:
            # print "INCREASE IN MIDDLE"
            # Increase size in middle
            self.arr = self.arr[:self.back + 1] + [None] * len(self.arr) + self.arr[self.front:]

            # Update front index
            self.front += len(self.arr) / 2


def test_9_8():
    # Tests CircularQueue Implementation
    queue = CircularQueue(5)

    # Add 10 elements
    for i in range(10):
        queue.enqueue(i)

    # Check size
    print len(queue) == 10

    # Remove 5 elements and ensure that they are the right numbers
    for i in range(5):
        out = queue.dequeue()
        if out!= i:
            print "Failure: Got %d Expected %d" % (out, i)
            return

    # Check size
    print len(queue) == 5

    # Add 3 elements
    for i in range(10,13):
        queue.enqueue(i)

    # Remove all elements and ensure they are the right number
    for i in range(5,13):
        out = queue.dequeue()
        if out!= i:
            print "Failure: Got %d Expected %d" % (out, i)
            return

    # Check size
    print len(queue) == 0

    # Make sure can't pop something else
    print queue.dequeue() is None

    # Increase size massively
    for i in range(100):
        queue.enqueue(i)

    # Pop everything and check
    for i in range(100):
        out = queue.dequeue()
        if out!= i:
            print "Failure: Got %d Expected %d" % (out, i)
            return

    # Check empty
    print len(queue) == 0

# Problem 9.4
def normalize_path(path):
    abs_path = path[0] == '/'
    tokens = path.rstrip('/').split('/')
    stack = Stack()

    for token in tokens:
        if token == '..':
            if stack.peek() in [None, '..']:
                stack.push(token)
            else:
                stack.pop()
        elif token in ['','.']:
            pass
        else:
            stack.push(token)

    output =''
    while stack.peek() is not None:
        output = stack.pop().data + '/' + output

    return '/' + output[:-1] if abs_path else output[:-1]

def test_9_4():
    simple_paths = ['/usr/bin/gcc','scripts/awkscripts','../../steve/public']
    cmplx_paths = ['/usr/lib/../bin/gcc','scripts//./../scripts/awkscripts/././','../../steve/./secret/../public']

    for simple, cmplx in zip(simple_paths, cmplx_paths):
        print simple == normalize_path(cmplx)

def main():
    # bintree_arr_test()
    # eval_RPN_test()
    # test_9_8()
    test_9_4()

if __name__ == '__main__':
    main()
