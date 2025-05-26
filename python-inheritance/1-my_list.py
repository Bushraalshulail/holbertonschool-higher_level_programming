#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from the built-in list.
It adds a method to print the list in ascending sort order without modify it.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It provides a method to print the list in ascending order.
    All elements in the list are expected to be integers.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        This method does not modify the original list.
        """
        print(sorted(self))
