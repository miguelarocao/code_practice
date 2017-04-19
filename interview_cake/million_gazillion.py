# Interview Cake: Million Gazillion
# https://www.interviewcake.com/question/python/compress-url-list
# Miguel Aroca-Ouellette
# 19/04/2017

# Use a trie, saves space when storing identical strings
#   O(k) worst case look up time where k is the length of the word

import Queue

class Trie:
    # Trie class
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                curr_node = curr_node.add_child(letter)

        curr_node.end = True

    def __str__(self):
        q = Queue.Queue()
        q.put((0, '', self.root))
        prev_depth = 0
        output = ''
        while not q.empty():
            depth, letter, node = q.get()
            if depth != prev_depth:
                prev_depth = depth
                output += '\n'

            output += ('[%s]' % letter) if node.end else letter
            for letter, node in node.children.iteritems():
                q.put((depth + 1, letter, node))

        return output

    def check_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]

        return curr_node.end

class TrieNode:
    # Trie Node Class
    def __init__(self):
        self.children = dict()
        self.end = False

    def add_child(self, letter):
        self.children[letter] = TrieNode()
        return self.children[letter]

    def set_end(self):
        self.end = True

# Add some words to the Trie
test = Trie()
test.add_word('APPLE')
test.add_word('APPIE')
test.add_word('APP')
test.add_word('LINUX')

# Print Trie
print test
print ''

# Test a couple words which are in Trie
print test.check_word('APP')
print test.check_word('APPLE')

# Test a few which aren't
print test.check_word('APPL')
print test.check_word('B')