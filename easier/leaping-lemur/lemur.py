"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branches (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5

    NOTES:
    starting at the first branch, the lemur can either jump to the next branch or to the branch after
    the lemur cannot jump to the branch if the branch is dead (1)
    this will determine if the lemur jumps to the next branch or to the branch after
    ideally, we'd like to get to the last tree as quickly as possible, so if the branch two jumps away isn't dead, we want to do that
    if the branch two jumps away IS dead from the branch we are on currently, then we can only make one jump
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    current_branch = 0
    jumps = 0

    if len(branches) == 2:
        return 1

    while current_branch < len(branches)-2:
        if branches[current_branch+2] != 1:
            current_branch += 2
            jumps += 1
        else:
            current_branch += 1
            jumps += 1

    return jumps



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")