"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.
Given a lemming in any of these  holes, who has to travel the farthest?

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2

    >>> furthest_optimized(7, [0, 6])
    3

    NOTES:
    1    2   3
    [0] [1] [2]

    1    2   3   4   5   6
    [0] [1] [2] [3] [4] [5]

    
    7, [0, 6] => 3

    c h h h h h c


    3, [0]  => 2

    c h h


    3, [1] => 1

    h c h


    3, [2] => 2

    h h c

    4, [1] =>

    h c h h 
    
    6, [2, 4] => 2

    h h c h c h

    h c h h h h c h 
    

    when you are at a cafe, how far away do you have to go until you start to get closer to another cafe?
    find midpoint between cafes

    if there is 1 cafe, the distance is whichever section of holes on either side is longer
    so if there are num_holes and the second one (cafes[1]) is a cafe, then the set of holes before the cafe have the length of the index of the cafe
    and the holes after have the length of the num_holes - 1 - index of the cafe

    if there are two cafes, the distance is whichever is longer: length until the first cafe, length until the last cafe, length between each cafe/2
    three lengths: first cafe index, num_holes - 1 - index of cafe, distance between each pair of cafes/2

    compare all of these distances, and return whichever is the longest

    OPTIMIZED:
    ???
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    if num_holes == len(cafes):
        return 0

    distance_to_first_cafe = cafes[0]
    distance_to_last_cafe = num_holes - 1 - cafes[-1]

    if len(cafes) == 1:
        return max(distance_to_first_cafe, distance_to_last_cafe)
    else:
        max_distance = 0

        for i in range(len(cafes)):
            distance_between_cafes = (cafes[i] - cafes[i-1]) // 2
            max_distance = max(distance_to_first_cafe, distance_to_last_cafe, distance_between_cafes)

    return max_distance

def furthest_optimized(num_holes, cafes):
    """Optimized version of above solution."""

    # Can this be optimized?

    pass


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
