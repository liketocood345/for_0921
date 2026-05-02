# This function prints all dictionary words that contain all letters
# in the string required_letters at least once.  A word may contain
# other letters as well, and may contain repeated letters, but for every
# character c in required_letters, the word must contain at least one
# occurrence of c.
#
# The words are printed in strictly increasing order of their length,
# and for a given length, in alphabetical order.  One word is printed
# per line, with no trailing spaces.
#
# You can assume that:
#   - required_letters is a string of uppercase letters,
#   - dictionary.txt is stored in the working directory,
#   - every word in dictionary.txt consists of uppercase letters only.
#
# The output is printed out, not returned.


dictionary_file = 'dictionary.txt'


def words_containing_all(required_letters):
    '''
    >>> words_containing_all('JQ')
    JACQUES
    JOAQUIN
    JONQUIL
    JACQUELINE
    >>> words_containing_all('JX')
    AJAX
    JUXTAPOSE
    JUXTAPOSED
    JUXTAPOSES
    JUXTAPOSING
    >>> words_containing_all('QW')
    SQUAW
    SQUAWK
    SQUAWKS
    SQUAWKED
    SQUAWKING
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
