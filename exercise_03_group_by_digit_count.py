# This function groups the integers in a list according to how many
# digits they have. The groups are processed from the smallest number
# of digits to the largest.
#
# Within each group, the numbers appear in the same order as in the
# original list.
#
# For grammatical correctness:
#   • Use "1 digit" when a group has size 1, otherwise "X digits".
#   • Use "Number" when the group contains a single element,
#     otherwise "Numbers".
#
# You can assume that the argument to group_by_digit_count() is a list
# of integers, all at least equal to 0.
#
# The output is printed out, not returned.


from collections import defaultdict


def group_by_digit_count(L):
    '''
    >>> group_by_digit_count([])
    >>> group_by_digit_count([7])
    Number with 1 digit: 7
    >>> group_by_digit_count([1, 22, 345, 9, 44, 808, 7])
    Numbers with 1 digit: 1 9 7
    Numbers with 2 digits: 22 44
    Numbers with 3 digits: 345 808
    >>> group_by_digit_count([100, 55, 20, 4282, 135])
    Numbers with 2 digits: 55 20
    Numbers with 3 digits: 100 135
    Number with 4 digits: 4282
    >>> group_by_digit_count([2, 22, 222, 3, 33, 4444, 55555, 7])
    Numbers with 1 digit: 2 3 7
    Numbers with 2 digits: 22 33
    Number with 3 digits: 222
    Number with 4 digits: 4444
    Number with 5 digits: 55555
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
