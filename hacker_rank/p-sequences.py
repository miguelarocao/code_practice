# Miguel Aroca-Ouellette
# 06/06/2016
# https://www.hackerrank.com/challenges/p-sequences

import timeit as ti

'''
The solutions below are ordered in the way I tried them.
'''

'''
RECURSIVE SOLUTION:
Naively recurses through the problem and counts.
Used as a baseline to compare other solutions against.
Test passed on HackerRank: 10%.
'''

# global
pairs = {}
seq_count = 0


def get_num_rec(N, P):
    # N -> length
    # P -> P-seq bound
    # step 1: solve for every pair
    val_nums = range(1, P + 1)
    for i in val_nums:
        for j in val_nums:
            if i * j > P:
                break
            try:
                pairs[i].append(j)
            except KeyError:
                pairs[i] = [j]

    # recursive list build & count
    for num in val_nums:
        pseq_count([num], N)
    return seq_count


# recursively builds and counts p-sequences based on valid pairs
def pseq_count(pseq, N):
    global seq_count
    # base case
    if len(pseq) == N:
        seq_count += 1
        return

    # check possible next values
    for num in pairs[pseq[-1]]:
        pseq_count(list(pseq + [num]), N)

'''
DYNAMIC PROGRAMMING SOLUTION:
Maintain stack of problems to solve and store sub-solutions for use in future.
For example: The number of possible sequences emanating from 11111... is the same as the number of sequences
             emanating from 22221..., therefore we can reuse that sub-solution. (Assuming N>5)
As expected this encounters similar memory issues to the recursive approach, although it saves on computation time.
HackerRank tests passed: 10%
'''

def get_num_dp(N, P):
    trans = [[0]]
    groups = [0]
    groups_size = [0]

    curr_group = range(1, P + 1)
    trans.append(list(curr_group))
    groups.append(1)
    groups_size.append(0)
    group_map = [0] * (P + 1)
    group_idx = 1
    for i in range(1, P + 1):
        if (curr_group[-1] * i) > P:
            while (curr_group[-1] * i) > P:
                curr_group.pop()  # pop last item
            trans.append(list(curr_group))
            groups.append(i)
            groups_size.append(0)
            group_idx += 1
        groups_size[-1] += 1
        group_map[i] = group_idx

    # convert trans to groups
    trans_size = [[] for _ in range(len(trans))]
    trans_size[0] = [0]
    for i, ls in enumerate(trans):
        new_list = [group_map[item] for item in ls]
        trans[i] = list(set(new_list))
        trans_size[i] = [new_list.count(item) for item in trans[i]]

    # stack where future actions will be stored
    stack = []

    # memory for dynamic programming.
    #   Key is "Num1,Num2,Depth" i.e. 1,6,10. Depth > 0 and refers to Num1
    #   Value is number of sequences at this point
    dp_mem = {}

    # push initial steps on stack BACKWARDS
    depth = 1
    for i in xrange(len(trans) - 1, 0, -1):
        push_all(stack, i, trans, depth)

    # while stack isnt empty!
    while stack:
        curr_solve = stack.pop()
        # check memory if it has already been solved
        if curr_solve in dp_mem:
            continue
        else:
            # need to solve!
            curr_num, next_num, depth = map(int, curr_solve.split(','))

            # check if last level, if so then solve
            if (depth + 1) == N:
                dp_mem[curr_solve] = groups_size[next_num]
                continue

            # push problem back on stack
            stack.append(curr_solve)

            # check if transitions are in memory
            trans_ls = str_trans(next_num, trans, depth + 1)
            if all(mem in dp_mem for mem in trans_ls):
                # if so then solve
                curr_sum = 0
                for mem in trans_ls:
                    curr_sum += dp_mem[mem] * groups_size[next_num]
                dp_mem[to_str(curr_num, next_num, depth)] = curr_sum % (10 ** 9 + 7)
            else:
                # otherwise push non-solved to stack
                for mem in trans_ls:
                    if mem not in dp_mem:
                        stack.append(mem)

    # get sum of root nodes
    count = 0
    for i in range(1, len(trans)):
        for j in trans[i]:
            count += dp_mem[str(i) + ',' + str(j) + ',1'] * groups_size[i]

    return count % (10**9+7)


def to_str(curr_num, next_num, depth):
    # converts to appropriately formatted string
    return ','.join(map(str, [curr_num, next_num, depth]))


def str_trans(num, trans, depth):
    # returns a list of string versions of the transition from a number at a specific depth
    #   output is in reversed order
    out = []
    for j in trans[num][::-1]:
        out.append(to_str(num, j, depth))
    return out


def push_all(stack, num, trans, depth):
    # pushes all the transitions from number num to stack
    stack += str_trans(num, trans, depth)


'''
NON-RECURSIVE SOLUTION v1:
Builds transition matrices between each possible number.
At every step in N the count of each number is updated based on the transition matrices and the current count.
Much better in terms of memory.
HackerRank tests passed: 50%
'''


def non_rec_v1(N, P):
    # get next trans
    trans = [[] for _ in range(0, P + 1)]  # 0 index should always be empty
    trans[0] = 0
    for i in range(1, P + 1):
        for j in range(1, P + 1):
            if i * j > P:
                break
            trans[i].append(j)

    count = [1] * (P + 1)  # count 0 should be None
    count[0] = 0
    for i in range(N - 1):
        new_count = [0] * (P + 1)  # new_count 0 should be None
        new_count[0] = 0
        for j in range(1, P + 1):
            for num in trans[j]:
                new_count[num] += count[j]

        count = [num % (10 ** 9 + 7) for num in new_count]


    return sum(count[1:]) % (10**9+7)


'''
NON-RECURSIVE SOLUTION v2:
Same as above, but groups numbers based on similar transitions, this saves on time and space complexity.
Reduces the set of numbers/groups to consider at each time step down to ~2*Sqrt(P).
HackerRank tests passed: 50%
'''

def non_rec_v2(N, P):
    trans = [[0]]
    groups = [0]
    groups_size = [0]
    for i in range(1, P + 1):
        new_group = []
        for j in range(1, P + 1):
            if i * j > P:
                break
            new_group.append(j)
        # check if group exists
        nearest = near_greater(groups, i)
        if trans[nearest - 1] != new_group:
            groups.insert(nearest, i)
            trans.insert(nearest, new_group)
            groups_size.insert(nearest, 1)
        else:
            groups_size[nearest - 1] += 1

    # once groups are completed build num -> group mapping
    group_map = [0] * (P + 1)
    group_idx = 1
    for i in range(1, P + 1):
        if (group_idx + 1) < len(groups) and i == groups[group_idx + 1]:
            group_idx += 1
        group_map[i] = group_idx

    # convert trans to groups
    trans_size = [[] for _ in range(len(trans))]
    trans_size[0] = [0]
    for i, ls in enumerate(trans):
        new_list = [group_map[item] for item in ls]
        trans[i] = list(set(new_list))
        trans_size[i] = [new_list.count(item) for item in trans[i]]

    count = list(groups_size)

    for i in range(N - 1):
        new_count = [0] * len(groups_size)  # new_count 0 should be None
        for j in range(1, len(trans)):  # skip the 0
            # for every transfer set
            for k in range(len(trans[j])):
                new_count[trans[j][k]] += count[j] * trans_size[j][k]
        count = [num % (10 ** 9 + 7) for num in new_count]

    # get total count
    tot_count = 0
    for i in range(len(count)):
        tot_count += count[i]

    return tot_count % (10 ** 9 + 7)


def near_greater(ls, num):
    # finds the smallest number in the list which is greater than the input number
    # returns index of that number (and len(list+1) if no such number exists)
    # input list should be ordered!
    assert (ls != [])

    i = 0
    for i, val in enumerate(ls):
        if val > num:
            return i

    return i + 1

'''
NON-RECURSIVE SOLUTION v3:
More efficient version of v2, builds number to group mapping and transitions simultaneously.
Building transitions backwards also saves on time and memory since some groups can be populated in the process.
HackerRank tests passed: 50%
'''


def non_rec_v3(N, P):
    trans = [[[0], []]]  # known, unknown
    groups = [0]
    groups_size = [0]

    curr_group = [[], [1]]
    curr_mult = 1
    trans.append([list(item) for item in curr_group])
    groups_size.append(0)
    group_map = [0] * (P + 1)
    group_idx = 1

    curr_mult += 1
    i = P
    for i in xrange(P, 0, -1):  # go backwards
        if (curr_mult * i) > P:
            group_map[i] = group_idx
            groups_size[-1] += 1
            continue
        while (curr_mult * i) <= P:
            if group_map[curr_mult] != 0:
                # known, append group
                curr_group[0].append(group_map[curr_mult])  # add last item to group
                if group_map[curr_mult] == 1:
                    break
            else:
                # unknown, append number
                curr_group[1].append(curr_mult)
            curr_mult += 1

        trans.insert(1, [list(item) for item in curr_group])
        groups.insert(1, i + 1)
        groups_size.append(1)
        group_idx += 1
        group_map[i] = group_idx

    groups.insert(1, i)

    # convert trans to groups
    trans_size = [[] for _ in range(len(trans))]
    trans_size[0] = [0]
    for i, ls in enumerate(trans):
        new_list = [group_map[item] for item in ls[1]]
        new_list += ls[0]
        trans[i] = list(set(new_list))
        trans_size[i] = [groups_size[item] for item in trans[i]]  # because groups are backwards

    count = list(groups_size)

    for i in range(N - 1):
        new_count = [0] * len(groups_size)  # new_count 0 should be None
        for j in range(1, len(trans)):  # skip the 0
            # for every transfer set
            for k in range(len(trans[j])):
                new_count[trans[j][k]] += count[-j] * trans_size[j][k]  # -j due to reverse order
        count = [num % (10 ** 9 + 7) for num in new_count]

    # get total count
    tot_count = 0
    for i in range(len(count)):
        tot_count += count[i]

    return tot_count % (10**9+7)

'''
Final Submission: See function for explanation.
Key idea: Don't need to maintain transition matrices because each group (as used above) can be matched with a set
          of other allowed groups for the next iteration and incremented accordingly. This can be done even more
          efficiently be maintaining a cumulative count of sequences in each group, that way they do not have to
          be added up at each iteration (since the groups increase in size monotonically).
          This SIGNIFICANTLY decreases computation time, because we now need 1 less forloop when iterating through
          the time steps/groups.
          It also allows us to do away completely with building groups and transitions.
HackerRank tests passed: 89%
'''


def get_num_final(N, P):
    """ Maintain 2 types of numbers.
    Unique numbers which have a unique list of multiples which yield <=P.
    Non-unique numbers which are grouped together by their multiples which yield <=P.
    Two lists:
        (Note: "i" is the list index)
        uni_num: This list is populated by the # of unique numbers <=i in our current sequence tree level N.
                 Each increasing entry represents a larger aggregate of unique numbers.
        all_num: This list is populated by the # of numbers <=P/i in our current sequence tree level N.
                 Each decreasing entry represents a larger aggregate of groups and unique numbers.
                 For example i=1 includes all unique numbers and all groups of numbers.
    Note: Each list is of size sqrt(P).
    Insight: The next iteration of uni_num depends on the current values of all_num, and the next iteration of all_num
             depends on the current iteration of all_num.
    Method: Iterate through each time step, using uni_num to update all_num and all_num to update uni_num at the new
            time step.
    """

    # List size
    ls_size = int(P ** 0.5) + 1

    # Populate. Index 0 is unused
    curr_uni_num = [i for i in range(ls_size)]
    curr_all_num = [P / i for i in range(1, ls_size)]
    curr_all_num.insert(0, 0)

    # Create list of non-unique group sizes
    group_sizes = [(P / (i - 1) - P / i) for i in range(2, ls_size)]
    group_sizes.insert(0, 0)
    group_sizes.append(curr_all_num[-1] - curr_uni_num[-1])

    # Iterate through N:
    prev_uni_num = list(curr_uni_num)
    prev_all_num = list(curr_all_num)
    for n in range(N - 1):
        # update uni_num using all_num
        for i in range(1, ls_size):
            curr_uni_num[i] = (prev_all_num[i] + curr_uni_num[i - 1]) % (10 ** 9 + 7)

        # update all_num using uni_num
        curr_all_num[-1] = (curr_uni_num[-1] + prev_uni_num[-1] * group_sizes[-1]) % (10 ** 9 + 7)
        for i in xrange(ls_size - 2, 0, -1):
            curr_all_num[i] = (prev_uni_num[i] * group_sizes[i] + curr_all_num[i + 1]) % (10 ** 9 + 7)

        # swap current and previous
        prev_uni_num = list(curr_uni_num)
        prev_all_num = list(curr_all_num)

    return curr_all_num[1]


def main():
    # For use on HackerRank simply get N & P using int(raw_input()) and print the result of function used.

    # Sample results
    print "Sample results for N=10, P=10(should all be identical):"
    # These two very slow for large N or P
    N, P = 10, 10
    print get_num_rec(N, P)
    print get_num_dp(N, P)

    # These are much faster
    print non_rec_v1(N, P)
    print non_rec_v2(N, P)
    print non_rec_v3(N, P)
    print get_num_final(N, P)

    print "\nTiming 10 iterations of N=1000, P=10000 (in seconds)..."
    # Timing of the faster ones
    print "V1: " + str(ti.timeit('non_rec_v1(1000,10000)', setup="from __main__ import non_rec_v1", number=10))
    print "V2: " + str(ti.timeit('non_rec_v2(1000,10000)', setup="from __main__ import non_rec_v2", number=10))
    print "V3: " + str(ti.timeit('non_rec_v3(1000,10000)', setup="from __main__ import non_rec_v3", number=10))
    print "Final: " + str(ti.timeit('get_num_final(1000,10000)', setup="from __main__ import get_num_final", number=10))

if __name__ == '__main__':
    main()
