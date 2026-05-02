# This function returns all strictly increasing-absolute-value sublists of the
# list L passed as argument. A sublist follows the rule if each element
# has strictly greater absolute value than the one before it:
#
#       |a₁| < |a₂| < |a₃| < ...
#
# Single-element sublists always satisfy the rule.
#
# Sublists with identical values may occur more than once if they come
# from different positions in L.
#
# The sublists are returned in the order naturally determined by this
# process: all sublists starting at index 0 (in the order in which they
# are extended to the right), then all sublists starting at index 1, and
# so on.
#
# You can assume that the argument to abs_increasing_sublists() is a
# list of integers (positive, zero, or negative).
#
# The output is returned, not printed.


def abs_increasing_sublists(L):
    '''
    >>> abs_increasing_sublists([])
    []
    >>> abs_increasing_sublists([4])
    [[4]]
    >>> abs_increasing_sublists([1, 2])
    [[1], [1, 2], [2]]
    >>> abs_increasing_sublists([-1, 3, -5])
    [[-1], [-1, 3], [-1, 3, -5], [3], [3, -5], [-5]]
    >>> abs_increasing_sublists([2, -1, 4])
    [[2], [-1], [-1, 4], [4]]
    >>> abs_increasing_sublists([1, 1, 2])
    [[1], [1, 2], [1], [1, 2], [2]]
    >>> abs_increasing_sublists([3, -2, -1])
    [[3], [-2], [-1]]
    >>> abs_increasing_sublists([-2, 3, 1, -4])
    [[-2], [-2, 3], [-2, 3, -4], [3], [3, -4], [1], [1, -4], [-4]]
    >>> abs_increasing_sublists([0, 1, 0])
    [[0], [0, 1], [1], [0]]
    '''
    return []
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
