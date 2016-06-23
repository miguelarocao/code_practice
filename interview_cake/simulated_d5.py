# Interview Cake: Simulated 5-Sided Die
# https://www.interviewcake.com/question/python/simulate-5-sided-die
# Miguel Aroca-Ouellette
# 06/22/2016

import random as rnd


# For use in solution
def rand7():
    return rnd.randint(1, 7)


# Solution
def rand5():
    """ Return a random integer in range [1,5] with equal probability, using only rand7()
        Space complexity: O(1)
        Time complexity: Worst Case: Infinity"""
    while True:
        curr_num = rand7()
        if curr_num <= 5:
            return curr_num

'''
Proving that this works is easy, simply use infinite geometric sequences:
for all n in N={1,2,3,4,5}:
P(n) = (1/7) + (1/7)(2/7) + (1/7)(2/7)^2 + ...
P(n) = (1/7)(1/(1 - (2/7))
P(n) = (1/7)/(5/7) = (1/5)

-----

Outline of proof that you can't have a solution which is guaranteed to terminate:
Disclaimer: I haven't done a lot of number of theory so this might be way off.

Let's assume that you could have a finite sequence (or combination of sequences) of flips which allows
you to generate an integer with probability 1/5.

The probability of the number yielded by that sequence would have to be of the form:
P(n) = sum_i( 1/(7^x_i) ) for some set of integers x_i
     = a/(7^b)            for some integers a and b

We therefore need a*5 = (7^b). But this is impossible since the number (7^b) cannot have 5 as a factor
by the fundamental theorem of arithmetic and the fact that both 5 and 7 are prime.

Therefore no solution is guaranteed to terminate.

'''

# Quantitative Test
test_bins = [0]*5
num_test = 100000
thresh = 1e-2
for i in range(num_test):
    test_bins[rand5() - 1] += 1.0/num_test

# Should all be roughly equal to 0.2
print test_bins
if all(abs((1.0/5) - item) < thresh for item in test_bins):
    print "Test passed."
else:
    print "Test failed."
