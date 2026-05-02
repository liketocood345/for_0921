# This class models an item stored in an inventory, with a name and a
# non-negative number of units currently in stock. The class enforces
# that the stock can never become negative, and that stock adjustments
# must always be given as positive integers.
#
# A single class-specific exception is defined:
#
#   - InventoryError
#       Raised whenever an invalid operation is attempted. The specific
#       reason for the error is conveyed through the exception message:
#
#           "Item name must be a string"
#           "Negative initial stock"
#           "Stock adjustment must be positive"
#           "Insufficient stock"
#
# The class provides the following methods:
#
#   - add_stock(n)
#       Increases the number of units in stock by n. Raises
#       InventoryError with message "Stock adjustment must be positive"
#       if n <= 0.
#
#   - remove_stock(n)
#       Decreases the number of units in stock by n. Raises
#       InventoryError with message "Stock adjustment must be positive"
#       if n <= 0, and with message "Insufficient stock" if n is greater
#       than the current stock.
#
#   - get_stock()
#       Returns the current number of units in stock.
#
# The output of these methods is returned, not printed.


class InventoryError(Exception):
    pass


class InventoryItem:
    '''
    >>> item = InventoryItem("Widget", 10)
    >>> item.get_stock()
    10
    >>> item.add_stock(5)
    >>> item.get_stock()
    15
    >>> item.remove_stock(4)
    >>> item.get_stock()
    11
    >>> item.add_stock(0)
    Traceback (most recent call last):
    ...
    InventoryError: Stock adjustment must be positive
    >>> item.remove_stock(0)
    Traceback (most recent call last):
    ...
    InventoryError: Stock adjustment must be positive
    >>> item.remove_stock(20)
    Traceback (most recent call last):
    ...
    InventoryError: Insufficient stock
    >>> bad_item = InventoryItem("Bad", -3)
    Traceback (most recent call last):
    ...
    InventoryError: Negative initial stock
    >>> no_name_item = InventoryItem(123, 5)
    Traceback (most recent call last):
    ...
    InventoryError: Item name must be a string
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
