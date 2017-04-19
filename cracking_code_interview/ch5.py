# Chapter 5 problems

import sys

BITS_PER_BYTE = 8


# Problem 5.3
def find_next_largest(number):
    # Find next largest binary number with the same number of 1s

    assert isinstance(number, int)

    int_bits = sys.getsizeof(int()) * BITS_PER_BYTE
    c0 = 0
    c1 = 0
    i = 0

    # Iterate until leftmost 0 to the left of a 1 is found
    mask = 1
    in_ones = False
    while i < int_bits:
        if in_ones and mask & number == 0:
            break
        elif mask & number > 0:
            in_ones = True

        if in_ones:
            c1 +=1
        else:
            c0 += 1

        i += 1
        mask = mask << 1

    # Set the 0 to 1
    output = number | (1<<i)

    # Clear the numbers to the right of that 0
    output = output & (~((1<<i) - 1))

    # Shift in (c1 - 1) ones
    output = output | ((1<<(c1 - 1)) - 1)

    return output

def main():
    # Test for find_nearest_binaries
    number = 0b11011001111100
    larger = find_next_largest(number)
    print bin(larger)
    #larger, smaller = find_nearest_binaries(number)

    # print "Larger: " + bin(larger) + " Smaller: " + bin(smaller)

if __name__ == '__main__':
    main()