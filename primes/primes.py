"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []
    number_to_check = 2

    while len(primes) < count:
        # check if number is prime
        # if prime, add to list
        # if not prime, move on
        # increment number to check
        
        is_prime = True

        for num in range(2,number_to_check):
            if number_to_check % num == 0 and num != number_to_check:
                is_prime = False
                break
        
        if is_prime == True:
            primes.append(number_to_check)

        number_to_check += 1

    return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
