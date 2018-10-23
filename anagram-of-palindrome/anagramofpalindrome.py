"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_dict = {}
    
    for letter in word:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    # print(letter_dict)

    if len(word) <= 1:
        return True

    k_sum = 0
    v_sum = 0

    for k,v in letter_dict.items():
        k_sum += 1
        v_sum += v

    if v_sum <= k_sum:
        return False
    else:
        if k_sum % 2 == 0 and v_sum % 2 == 1:
            return True
        elif k_sum % 2 == 1 and v_sum % 2 == 0:
            return False
        elif k_sum % 2 == 0 and v_sum % 2 == 0:
            return True
        elif k_sum % 2 == 1 and v_sum % 2 == 1:
            return False






        






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
