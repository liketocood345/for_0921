# This function returns the number of contiguous runs of 1-bits
# in the binary representation of the argument.
#
# A "run" is a maximal consecutive sequence of 1s.
#
# For instance:
# 0:     0        → 0 runs
# 1:     1        → 1 run
# 2:    10        → 1 run
# 3:    11        → 1 run
# 4:   100        → 1 run
# 5:   101        → 2 runs
# 6:   110        → 1 run
# 7:   111        → 1 run
# 9:  1001        → 2 runs
# 13: 1101        → 2 runs
# 27: 11011       → 2 runs
#
# You can assume that the argument to count_runs() is an integer
# at least equal to 0.
#
# The output is returned, not printed.


def count_runs(n):
    '''
    >>> count_runs(0)
    0
    >>> count_runs(1)
    1
    >>> count_runs(2)
    1
    >>> count_runs(3)
    1
    >>> count_runs(4)
    1
    >>> count_runs(5)
    2
    >>> count_runs(6)
    1
    >>> count_runs(7)
    1
    >>> count_runs(9)
    2
    >>> count_runs(13)
    2
    >>> count_runs(37)
    3
    '''
    return -1
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
