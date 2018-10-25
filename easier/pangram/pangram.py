"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False

    NOTES:
    letters can appear mroe than once, but every letter from the alphabet must be included 
    keep a list of all letters seen, turn into set (for uniqueness), then if at the end of the string the length of the set is == 26, return True
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    letters_seen = set()

    for char in sentence.lower():
        if char.isalpha():
            letters_seen.add(char)
            if len(letters_seen) == 26:
                return True

    return False

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
