# This function returns the list of all distinct consecutive sublists of
# length k in the list L passed as argument. A consecutive sublist is a
# slice of L consisting of k elements that appear next to one another in L.
#
# Sublists that are identical as lists are kept only once, even if they
# occur several times in L. The distinct sublists returned are ordered in
# lexicographic order (as lists of integers).
#
# You can assume that:
#   - the argument L is a list of integers,
#   - the argument k is an integer such that 0 ≤ k ≤ len(L).
#
# The output is returned, not printed.


def consecutive_sublists(L, k):
    '''
    >>> consecutive_sublists([], 0)
    [[]]
    >>> consecutive_sublists([7, 7, 7, 7], 1)
    [[7]]
    >>> consecutive_sublists([4, 1, 7, 4], 1)
    [[1], [4], [7]]
    >>> consecutive_sublists([4, 1, 7], 2)
    [[1, 7], [4, 1]]
    >>> consecutive_sublists([4, 1, 7], 3)
    [[4, 1, 7]]
    >>> consecutive_sublists([2, 3, 5, 8], 2)
    [[2, 3], [3, 5], [5, 8]]
    >>> consecutive_sublists([1, 1, 1], 2)
    [[1, 1]]
    >>> consecutive_sublists([5, 2, 5], 2)
    [[2, 5], [5, 2]]
    >>> consecutive_sublists([1, 2, 3, 4, 5], 4)
    [[1, 2, 3, 4], [2, 3, 4, 5]]
    '''
    return []
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
