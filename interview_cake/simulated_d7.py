# Interview Cake: Simulated 7-Sided Die
# https://www.interviewcake.com/question/python/simulate-7-sided-die
# Miguel Aroca-Ouellette
# 06/29/2016

import random as rnd

# For use in solution
def rand5():
    return rnd.randint(1, 5)


# Solution
def rand7():
    """ Return a random integer in range [1,7] with equal probability, using only rand5()
        Space complexity: O(1)
        Time complexity: Worst Case: Infinity"""

    while True:
        roll1 = rand5()
        roll2 = rand5()
        num = (roll1 - 1)*5 + (roll2) #get number in [1,25] with uniform probability
        if num <= 21:
            # keep since 21 is divisible by 7
            return num % 7 + 1

'''
Proving that this works is easy, simply use infinite geometric sequences:
for all n in N={1,2,3,4,5,6,7} (using rand5() twice so the probability is 1/25 for every number):
P(n) = (1/25) + (1/25)(18/25) + (1/25)(18/25)^2 + ...
P(n) = (1/25)(1/(1 - (18/25))
P(n) = (1/25)/(25/7) = (1/7)

-----

Outline of proof that you can't have a solution which is guaranteed to terminate:

Same as for "simulated_d5.py".

'''


# Quantitative Test
test_bins = [0]*7
num_test = 100000
thresh = 1e-2
for i in range(num_test):
    test_bins[rand7() - 1] += 1.0/num_test

# Should all be roughly equal to 0.2
print test_bins
if all(abs((1.0/7) - item) < thresh for item in test_bins):
    print "Test passed."
else:
    print "Test failed."
