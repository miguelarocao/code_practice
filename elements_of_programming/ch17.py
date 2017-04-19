# Chapter 17 Problems

import timeit


# Problem 17.1
def combo_scores(final, play_scores, cache):
    # Base cases
    if play_scores == []:
        return 0
    elif len(play_scores) == 1:
        return 1 if final % play_scores[0] == 0 else 0

    output = 0
    for i in range(final / play_scores[-1] + 1):
        new_final = final - play_scores[-1] * i
        key = (new_final, play_scores[-1])

        if key not in cache:
            cache[key] = combo_scores(new_final, play_scores[:-1], cache)

        output += cache[key]

    return output


def combo_handler(final, play_scores):
    cache = {}
    sort_play_scores = play_scores  # sorted(play_scores) # assume sorted for now

    return combo_scores(final, sort_play_scores, cache)


# Better solution to 17.1
def combo_scores_better(final, play_scores):
    # Assumes play_scores is already sorted
    n = len(play_scores)

    A = [([1] + [0] * (final)) for _ in range(n)]

    for i in range(n):
        for j in range(1, final + 1):
            # handle case where i == 0:
            if i == 0:
                if j % play_scores[i] == 0:
                    A[i][j] = 1
            else:
                for k in range(j / play_scores[i] + 1):
                    A[i][j] += A[i - 1][j - k * play_scores[i]]

    return A[-1][-1]


# Best solution to 17.1
def combo_scores_best(final, play_scores):
    # Assumes play_scores is already sorted
    n = len(play_scores)

    A = [([1] + [0] * (final)) for _ in range(n)]

    for i in range(n):
        for j in range(1, final + 1):
            # handle case where i == 0:
            if i == 0:
                if j % play_scores[i] == 0:
                    A[i][j] = 1
            else:
                A[i][j] += A[i - 1][j]
                if j - play_scores[i] >= 0:
                    A[i][j] += A[i][j - play_scores[i]]

    return A[-1][-1]


def test_17_1():
    final = 10000
    play_scores = [2, 3, 7, 13, 25, 47, 123, 345, 1111, 1231]

    print combo_handler(final, play_scores)
    print combo_scores_better(final, play_scores)
    print combo_scores_best(final, play_scores)

    input_str = str(final) + ',[' + ','.join(map(str, play_scores)) + ']'
    print timeit.timeit('combo_handler(' + input_str + ')', setup='from __main__ import combo_handler', number=10)
    print timeit.timeit('combo_scores_better(' + input_str + ')', setup='from __main__ import combo_scores_better',
                        number=10)
    print timeit.timeit('combo_scores_best(' + input_str + ')', setup='from __main__ import combo_scores_best',
                        number=10)


# Problem 17.2
def levenshtein(str1, str2, idx1, idx2, cache):
    if idx1 < 0:
        return idx2 + 1
    elif idx2 < 0:
        return idx1 + 1

    if (idx1, idx2) not in cache:
        if str1[idx1] == str2[idx2]:
            cache[(idx1, idx2)] = levenshtein(str1, str2, idx1 - 1, idx2 - 1, cache)
        else:
            swap = levenshtein(str1, str2, idx1 - 1, idx2 - 1, cache)
            insert = levenshtein(str1, str2, idx1, idx2 - 1, cache)
            remove = levenshtein(str1, str2, idx1 - 1, idx2, cache)
            cache[(idx1, idx2)] = 1 + min([swap, insert, remove])

    return cache[(idx1, idx2)]


def levenshtein_handler(str1, str2):
    cache = {}
    return levenshtein(str1, str2, len(str1) - 1, len(str2) - 1, cache)


def test_17_2():
    str1 = "Saturday"
    str2 = "Sundays"

    print levenshtein_handler(str1, str2)


# Problem 17.3
def number_of_ways(n, m, i, j, cache):
    if i == (n - 1) and j == (m - 1):
        return 1

    output = 0
    for new_i, new_j in [(i + 1, j), (i, j + 1)]:
        if new_i < n and new_j < m:
            key = (new_i, new_j)
            if key not in cache:
                cache[key] = number_of_ways(n, m, new_i, new_j, cache)

            output += cache[key]

    return output


def number_of_ways_handler(n, m):
    cache = {}

    return number_of_ways(n, m, 0, 0, cache)


def test_17_3():
    n, m = (5, 5)
    print number_of_ways_handler(n, m)


# Problem 17.8
def triangle_shortest(triangle):
    cache = [None] * 2
    old_cache = [triangle[0][0]]
    greedy_min = float("inf")
    for k, arr in enumerate(triangle[1:]):
        for i in range(len(arr)):
            if (0 <= i < (len(arr) - 1)) and (0 <= (i - 1) < (len(arr) - 1)):
                cache[i] = min(old_cache[i], old_cache[i - 1]) + arr[i]
            elif 0 <= i < (len(arr) - 1):
                cache[i] = old_cache[i] + arr[i]
            else:
                cache[i] = old_cache[i - 1] + arr[i]

            if k == (len(triangle) - 2) and cache[i] < greedy_min:  # Last iteration
                greedy_min = cache[i]

        old_cache = list(cache)
        cache = [None] * (len(arr) + 1)

    return greedy_min if len(triangle) > 1 else triangle[0][0]


def test_17_8():
    triangle = [[2], [4, 4], [8, 5, 6], [4, 2, 6, 2], [1, 5, 2, 3, 4]]

    print triangle_shortest(triangle)


# Problem 17.6
class Clock:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return "C{%d,%d}" % (self.weight, self.value)


def clock_thief(clocks, max_weight, cache=None, use_cache=True):
    if use_cache:
        cache = cache if cache else {}

    # print "Analyzing " + str(clocks[0])

    # Base cases
    if len(clocks) == 1:
        return 0 if clocks[0].weight > max_weight else clocks[0].value

    key = (clocks[0], max_weight)
    if key not in cache or not use_cache:
        if clocks[0].weight <= max_weight:
            use_clock = clock_thief(clocks[1:], max_weight - clocks[0].weight, cache, use_cache) + clocks[0].value
        else:
            use_clock = 0
        no_clock = clock_thief(clocks[1:], max_weight, cache, use_cache)
        # print "Using %s -> %d, Not using %s -> %d" % (str(clocks[0]), use_clock, str(clocks[0]), no_clock)
        result = max(use_clock, no_clock)

        # print result

        if use_cache:
            cache[key] = result
    else:
        result = cache[key]

    return result


def clock_thief_table(clocks, max_weight):
    table = [[0] * (max_weight + 1) for _ in range(len(clocks))]

    # Fill in first clock
    for avail_weight in range(max_weight + 1):
        if clocks[0].weight <= avail_weight:
            table[0][avail_weight] = clocks[0].value

    for i, clock in enumerate(clocks):
        if i == 0:
            continue
        for avail_weight in range(max_weight + 1):
            if clock.weight > avail_weight:
                table[i][avail_weight] = table[i - 1][avail_weight]
            else:
                with_clock = table[i - 1][avail_weight - clock.weight] + clock.value
                without_clock = table[i - 1][avail_weight]
                table[i][avail_weight] = max(with_clock, without_clock)

    return table[-1][-1]


def test_17_6():
    clocks = [Clock(5, 60), Clock(3, 50), Clock(4, 70), Clock(2, 30)]

    print clock_thief(clocks, 5)
    print clock_thief_table(clocks, 5)

    clock_str = '[Clock(5, 60), Clock(3, 50), Clock(4, 70), Clock(2, 30)]'

    print timeit.timeit(setup='from __main__ import clock_thief, Clock', stmt='clock_thief(%s, %d)' % (clock_str, 50),
                        number=10000)
    print timeit.timeit(setup='from __main__ import clock_thief_table, Clock',
                        stmt='clock_thief_table(%s, %d)' % (clock_str, 50),
                        number=10000)


# Problem 17.5
def seq_in_2D_handler(pattern, matrix):
    cache = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if seq_in_2D(pattern, 0, r, c, matrix, cache):
                return True

    return False


def seq_in_2D(pattern, p_idx, r, c, matrix, cache):
    # Base case
    if p_idx == len(pattern) - 1:
        return pattern[p_idx] == matrix[r][c]

    # Check if doesn't match
    if matrix[r][c] != pattern[p_idx]:
        return False

    for change in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_r, new_c = r + change[0], c + change[1]
        if not (0 <= new_r < len(matrix)) or not (0 <= new_c < len(matrix[0])):
            continue

        key = (new_r, new_c, p_idx + 1)
        if key not in cache:
            cache[key] = seq_in_2D(pattern, p_idx + 1, new_r, new_c, matrix, cache)

        if cache[key]:
            return True

    return False


def seq_in_2D_table(pattern, matrix):
    table = [[[0] * len(matrix[0]) for _ in range(len(matrix))] for _ in range(len(pattern))]

    # Iterate through pattern and matrix
    for p, val in enumerate(pattern):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if p == 0:
                    # Special first case
                    table[p][r][c] = int(matrix[r][c] == val)
                else:
                    # Middle
                    if matrix[r][c] == val:
                        # Check surrounding values of previous layer
                        for prev_r, prev_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if not (0 <= prev_r < len(matrix)) or not (0 <= prev_c < len(matrix[0])):
                                continue

                            # Check previous layer for 1
                            if table[prev_r][prev_c][p - 1]:
                                # Special last case
                                if p == len(pattern) - 1:
                                    return True
                                table[r][c][p] = 1
                                break

    return False


def test_17_5():
    arr = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

    print seq_in_2D_handler([1, 3, 4, 6], arr)
    print seq_in_2D_handler([1, 2, 3, 4], arr)
    print seq_in_2D_table([1, 3, 4, 6], arr)
    print seq_in_2D_table([1, 2, 3, 4], arr)

    seq = [7, 4, 5, 3]

    print timeit.timeit(setup='from __main__ import seq_in_2D_handler', stmt='seq_in_2D_handler(%s, %s)' % (seq, arr),
                        number=10000)
    print timeit.timeit(setup='from __main__ import seq_in_2D_table', stmt='seq_in_2D_table(%s, %s)' % (seq, arr),
                        number=10000)

def pretty_print(str_words, max_char):
    words = str_words.split(' ')
    cache = {}

    mess_score, lines = pp_recur(words, 0, cache, max_char)
    print mess_score
    return lines

def pp_recur(words, idx, cache, max_char):
    ci = idx
    cc = 0
    while True:
        cc += len(words[ci])
        if cc > max_char:
            break
        cc += 1 # space
        ci += 1 # Go to next word
        if ci >= len(words):
            line = (' ').join(words[idx:])
            return (max_char - len(line))**2, [line]

    # Recurse over possible splits
    greedy_min = float("inf")
    output = None
    while idx < ci:
        curr_line = (' ').join(words[idx:ci])
        curr_mess = (max_char - len(curr_line))**2
        if curr_mess >= greedy_min:
            # Break since things will only get messier
            break

        # cache
        if ci not in cache:
            cache[ci] = pp_recur(words, ci, cache, max_char)

        mess, lines = cache[ci]
        if mess + curr_mess < greedy_min:
            greedy_min = mess + curr_mess
            output = [curr_line] + lines

        ci -= 1

    return greedy_min, output

def test_17_11():
    str_words ="I am a red dog" # test with 6
    str_words2 = ("I have inserted a large number of new examples from the papers "
                  "for the Mathematical Tripos during the last twenty years, which should be "
                  "useful to Cambridge students")

    output = pretty_print("aaa bbb c d ee ff ggggggg", 10)
    for line in output:
        print line

def longest_nondec(arr, idx = None, limit = float("inf"), cache = None):
    cache = {} if cache is None else cache
    idx = len(arr) - 1 if idx is None else idx

    if idx == 0:
        return 1 if arr[0] < limit else 0

    key_wo = (idx - 1, limit)
    key_w = (idx - 1, min(arr[idx], limit))
    if key_wo not in cache:
        cache[key_wo] = longest_nondec(arr, idx -1, limit, cache)
    if key_w not in cache:
        cache[key_w] = longest_nondec(arr, idx - 1, key_w[1], cache)

    output = None
    if arr[idx] < limit:
        output = max(cache[key_wo], cache[key_w] + 1)
    else:
        output = cache[key_wo]

    return output

def test_17_12():
    arr= [0,8,4,12,2,10,6,14,1,9]

    print longest_nondec(arr)


def main():
    # test_17_1()
    # test_17_2()
    # test_17_3()
    # test_17_8()
    # test_17_6()
    # test_17_5()
    # test_17_11()
    test_17_12()


if __name__ == '__main__':
    main()
