#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from the built-in list.
It adds a method to print the list in ascend sort order without modifying it.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It provides a method to print the list in ascending order.
    Assumes all list elements are integers.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
