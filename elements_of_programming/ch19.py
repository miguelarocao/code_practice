# Problem 19

from cracking_code_interview.Stack import Stack
from cracking_code_interview.Queue import Queue
import heapq as hp

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rel_coord(self, x_inc=0, y_inc=0):
        return Coord(self.x + x_inc, self.y + y_inc)

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

class Maze:
    def __init__(self, mtrx, start, end):
        self.mtrx = mtrx
        self.start = start
        self.end = end
        self.height = len(mtrx)
        self.width = len(mtrx[0])

    def pixel(self, coord):
        return self.mtrx[self.height - coord.y - 1][coord.x]

    def is_open(self, coord):
        assert isinstance(coord, Coord)

        return self.pixel(coord) == 1

    def in_bounds(self, coord):
        return 0 <= coord.x < self.width and 0<= coord.y < self.height

    def get_adj(self, coord):
        assert isinstance(coord, Coord)

        output = []
        rel_coords = [coord.rel_coord(x_inc, y_inc) for x_inc, y_inc in (-1, 0), (0, -1), (1, 0), (0, 1)]
        for rel_coord in rel_coords:
            if self.in_bounds(rel_coord) and self.is_open(rel_coord):
                output.append(rel_coord)

        return output


class Path:
    def __init__(self):
        self.path = []
        self.length = 0

    def end(self):
        if self.length > 0:
            return self.path[-1]
        else:
            return None

    def add(self, coord):
        self.path.append(coord)
        self.length += 1

    def shorten(self, n=1):
        self.path = self.path[:-n]
        self.length -= n
        self.length = max(self.length, 0)  # In case removed all nodes

    def contains(self, coords):
        for pixel in self.path:
            if pixel == coords:
                return True
        return False

    def __str__(self):
        return ', '.join(map(str, self.path))


def solve_maze(Maze):
    stack = Stack()
    path = Path()
    stack.push((Maze.start, 0))  # Store start and length of path not inclusive
    count = 0
    while True:
        next_pixel, length = stack.pop().data
        if path.length > length:
            path.shorten(path.length - length)
        path.add(next_pixel)
        adj = Maze.get_adj(next_pixel)
        for pixel in adj:
            if not path.contains(pixel):
                stack.push((pixel, length + 1))

        if path.end() == Maze.end:
            break

        if stack.top is None:
            # No path
            print "No path was found :("
            return

    print path

def test_maze():
    maze_mtrx = [[0, 0, 0],
                 [1, 1, 1],
                 [0, 0, 0]]


    my_maze = Maze(maze_mtrx, Coord(0, 1), Coord(2, 1))
    solve_maze(my_maze)


# Problem 19.7
def str_transform(start, goal, dictionary):
    queue = Queue()
    queue.enqueue((start, 0))
    checked = {start}
    while queue.first is not None:
        word, depth = queue.dequeue().data
        if word == goal:
            return depth
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in dictionary and new_word not in checked:
                    checked.add(new_word)
                    queue.enqueue((new_word, depth + 1))

    return -1

def test_19_7():
    start = 'bat'
    goal = 'dog'
    D ={'bat', 'cat','dog','bat','dot','cog','cot', 'bag'}

    print str_transform(start, goal, D) == 4
    print str_transform('foo', 'bag', D) == -1

# Problem 19.8
def enclosed(arr):
    # BFS for finding bounday
    queue = Queue()

    # Stack for keeping track of nodes to color
    stack = Stack()

    # Marks checked squares
    checked = [[False]*len(arr[0]) for _ in range(len(arr))]

    for r in range(1, len(arr) - 1):
        for c in range(1, len(arr[0]) - 1):
            if arr[r][c] == 'W' and not checked[r][c]:
                queue.enqueue((r, c))
                enclosed = True # Assume enclosed until proven otherwise
                while not queue.is_empty():
                    curr_r, curr_c = queue.dequeue().data
                    checked[curr_r][curr_c] = True
                    if on_boundary(arr, curr_r, curr_c):
                        print "%d %d not enclosed" % (curr_r, curr_c)
                        enclosed = False

                    stack.push((curr_r, curr_c))
                    for new_r, new_c in [(curr_r + 1, curr_c), (curr_r - 1, curr_c),
                                         (curr_r, curr_c + 1), (curr_r, curr_c - 1)]:
                        if arr[new_r][new_c] == 'W' and in_bounds(arr, new_r, new_c) and not checked[new_r][new_c]:
                            queue.enqueue((new_r, new_c))

                # empty stack
                while stack.peek() is not None:
                    curr_r, curr_c = stack.pop().data
                    print "%d %d stack pop from %d %d" % (curr_r, curr_c, r, c)
                    if enclosed:
                        arr[curr_r][curr_c] = 'B'

def on_boundary(arr, r, c):

    if r == 0 or r == len(arr) - 1:
        return True
    if c == 0 or c == len(arr[0]) - 1:
        return True

    return False

def in_bounds(arr, r, c):

    if (0 <= r < len(arr)) and (0 <= c < len(arr[0])):
        return True

    return False

def test_19_8():
    arr = [['B']*4, ['W','W','W','B'], ['B','W','W','B'], ['B']*4]

    enclosed(arr)

    for row in arr:
        print row

# Problem 19.9
class FrontierVertex:
    def __init__(self, vertex, cost, edge_count, path):
        self.vertex = vertex
        self.cost = cost
        self.edge_count = edge_count
        self.path = path

    # Modify comparison to take into account edge count if necessary
    def __cmp__(self, other):

        if self.cost == other.cost:
            return cmp(self.edge_count, other.edge_count)
        return cmp(self.cost, other.cost)

def dijkstraMod(V, E, cost, s, t):
    # Assumes E is in adjacency list format as a dictionary
    # Cost is (from, to) dictionary

    heap = []
    hp.heappush(heap, FrontierVertex(s, 0, 0, [s]))
    visited = {key: False for key in V}
    path = None
    # dijkstra
    while heap != []:
        curr = hp.heappop(heap)

        # Break if necessary
        if curr.vertex == t:
            path = list(curr.path)
            break

        # Skip if already visited through another (cheaper) path
        if visited[curr.vertex]:
            continue
        else:
            visited[curr.vertex] = True

        print "At vertex " + curr.vertex

        # Note: Could probably do better on memory if only stored each frontier vertex once
        #       Simply update the value of the frontier vertex by removing from heap and re-adding
        #       Only do this if new value is < than old value
        for next in E[curr.vertex]:
            if not visited[next]:
                hp.heappush(heap, FrontierVertex(next, curr.cost + cost[(curr.vertex, next)],
                                                 curr.edge_count + 1, curr.path + [next]))

    return path

def test_19_9():
    V = ['A', 'B', 'C', 'D', 'E', 'F']
    E = {'A': ['B', 'E'],
         'B': ['A', 'C'],
         'C': ['B', 'F', 'D'],
         'D': ['C', 'F', 'E'],
         'E': ['A', 'D'],
         'F': ['C', 'D']}

    cost = {('A', 'B'): 1,
            ('A', 'E'): 2,
            ('B', 'A'): 1,
            ('B', 'C'): 1,
            ('C', 'B'): 1,
            ('C', 'F'): 1,
            ('C', 'D'): 1,
            ('D', 'C'): 1,
            ('D', 'F'): 1,
            ('D', 'E'): 1,
            ('E', 'A'): 2,
            ('E', 'D'): 1,
            ('F', 'C'): 1,
            ('F', 'D'): 1}

    print dijkstraMod(V, E, cost, 'A', 'D')


def main():
    # test_19_7()
    test_19_9()

if __name__ == '__main__':
    main()