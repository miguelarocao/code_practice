# Interview Cake: Single Riffle Check
# https://www.interviewcake.com/question/python/single-rifle-check
# Miguel Aroca-Ouellette
# 02/11/2016

"""
Some thoughts:
For simplicity let's just say the deck has 6 cards labelled [1,2,3,4,5,6].
Then a single riffle might take the form:
    (1) Split into half_1 = [1,2,3] and half_2 = [4,5,6]
    (2) shuffled_deck = [1,2] + [4] = [1,2,4]
    (3) shuffled_deck = [3] + [5,6] + shuffled_deck = [3,5,6,1,2,4]

For consistency let's always label the half of the deck with smaller numbers as half_1.

Goal: Detect if the provided shuffled_deck is a single riffle.
Properties of a shuffled_deck which is formed by a single riffle:
    - The shuffled deck must be composed from the numbers in the original deck. (Each number once).
    - The shuffled deck must have 52 cards.
    - The shuffled deck is composed by a sequence of increasing subsequences since half_1 < half_2.
    - Can never have a decreasing subsequence of length > 2. (*)

Could also just try to undo the riffle. (*)
"""

import random

DECK_SIZE = 52


# Note: can do a little better by checking at every step if the shuffled deck matches one of the two riffle cards expected.
# Time and space complexity is the same however.
def check_riffle_undo(shuffled_deck):
    """
    Returns TRUE if deck can be formed from a single riffle. Else returns FALSE.
    Checks by undoing the riffle.
    """
    # Initialize
    decks = [[], []]
    curr_deck = 0

    i = 1
    decks[curr_deck].append(shuffled_deck[0])

    # Build half decks
    while i < DECK_SIZE and len(decks[0]) < (DECK_SIZE / 2) and len(decks[1]) < (DECK_SIZE / 2):
        # print "%d: %d %d" % (i, len(decks[0]), len(decks[1]))
        if (shuffled_deck[i] + 1 != shuffled_deck[i - 1]):
            curr_deck = (curr_deck + 1) % 2
        decks[curr_deck].append(shuffled_deck[i])
        i += 1

    # Check if valid
    if i > DECK_SIZE:
        return False

    decks[(curr_deck + 1) % 2] += shuffled_deck[i:]

    smaller, larger = (decks[0], decks[1]) if decks[0][0] < decks[1][0] else (decks[1], decks[0])

    if smaller == range(26, 0, -1) and larger == range(52, 26, -1):
        return True
    else:
        return False


# If you just stack the two halves
deck = range(52, 0, -1)

# If you alternate the two halves
other_deck = [None] * 52
other_deck[::2] = range(52, 26, -1)
other_deck[1::2] = range(26, 0, -1)

# Final test
test_deck = range(52, 38, -1) + range(26, 20, -1) + range(38, 30, -1) + range(20, 13, -1) + range(30, 26, -1) + range(
    13, 0, -1)

# Non-riffle
random.seed(12345)
bad_deck = range(52, 0, -1)
random.shuffle(bad_deck)

print check_riffle_undo(deck)
print check_riffle_undo(other_deck)
print check_riffle_undo(test_deck)
print check_riffle_undo(bad_deck) == False
