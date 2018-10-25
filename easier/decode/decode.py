"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'

    >>> decode("0h1ae2bcy3cato")
    'heyo'
"""


def decode(s):
    """Decode a string."""

    # number then letter
    # number signifies how many letters to skip

    # for 0h, take number, find and store letter 0+1 spot After
    # for 2anh, take number, find and store letter 2+1 spots after 
    # need to store indices and the number itself

    idx = 0
    i = 0

    decoded_string = ''

    for char in s:
        if not char.isdigit():
            idx += 1
        else:
            num_to_skip = int(char)
            idx += 1 
            decoded_string += s[idx + num_to_skip]


    return decoded_string
        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n")
