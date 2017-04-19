def sieve(max_num):
    # Returns a list of primes up to max_num (inclusive)

    flags = [True] * (max_num + 1)
    flags[0] = flags[1] = False

    curr_prime = 2

    while True:
        propagate_prime(flags, curr_prime)

        curr_prime = get_next_prime(flags, curr_prime)

        if curr_prime is None:
            break

    return [i for i in range(max_num + 1) if flags[i]]


def propagate_prime(flags, prime):
    # Sets flags to False on multiples of input 'prime'

    i = prime * 2
    while i < len(flags):
        flags[i] = False
        i += prime

    return


def get_next_prime(flags, num):
    # Returns the next prime number greater than the input number
    # Returns None if no primes < len(flags) is found

    for i in range(num + 1, len(flags)):
        if flags[i]:
            return i

    return None


print len(sieve(1000))
