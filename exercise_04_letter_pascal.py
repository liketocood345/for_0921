# This function prints the first n rows of Pascal's triangle, but with
# each entry converted to a letter of the alphabet.  The conversion is:
#
#       1 → A, 2 → B, 3 → C, …, 26 → Z, 27 → A, 28 → B, ...
#
# Each row is printed on its own line, visually centered.
# The letters in a row are separated by single spaces.
#
# In the printed output, no line has any trailing space.
#
# You can assume that the argument to letter_pascal() is an integer
# at least equal to 1.
#
# Reminder: In Pascal's triangle, any entry that is not on the boundary
# (i.e., not a 1 at the left or right edge) is equal to the sum of the two
# entries directly above it: the one above-left and the one above-right.
# This rule generates all the interior values of the triangle.
#
# The output is printed out, not returned.


from string import ascii_uppercase


def letter_pascal(n):
    '''
    >>> letter_pascal(1)
    A
    >>> letter_pascal(2)
     A
    A A
    >>> letter_pascal(3)
      A
     A A
    A B A
    >>> letter_pascal(4)
       A
      A A
     A B A
    A C C A
    >>> letter_pascal(6)
         A
        A A
       A B A
      A C C A
     A D F D A
    A E J J E A
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
