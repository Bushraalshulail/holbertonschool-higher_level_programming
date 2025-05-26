#!/usr/bin/python3
"""
This module defines the MyList class that inherits from the built-in list.
It includes a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList is a subclass of list that adds a method to print the list sorted.

    It assumes all elements are integers.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending
        sorted order without modifying the original list.
        """
        print(sorted(self))
