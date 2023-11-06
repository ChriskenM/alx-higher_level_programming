#!/usr/bin/python3

"""
Defiens a class.
"""
class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method prints the sorted list """

        print(sorted(self))
