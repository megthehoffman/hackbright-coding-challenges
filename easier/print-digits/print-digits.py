"""Given int, print each digit in reverse order, starting with the ones place. 

WITHOUT USING BUILT IN FUNCTIONS

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

    >>> no_strings_print_digits(1)
    1

    >>> no_strings_print_digits(413)
    3
    1
    4

    >>> no_strings_print_digits(7331)
    1
    3
    3
    7

    NOTES:

    print(num % 10 // 1)
    print(num % 100 // 10)
    print(num % 1000 // 100)
    print(num % 10000 // 1000)
    print(num % 100000 / 10000)

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    num_string = str(num)

    for i in range(1,len(num_string)+1):
        print(num_string[-i])


def no_strings_print_digits(num):
    """What if you couldn't turn the int into a str?"""

    i = 10

    while (num % i // (i // 10)) != 0:
        print(num % i // (i // 10))
        i *= 10


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
