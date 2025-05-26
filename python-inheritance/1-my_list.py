#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It includes a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Does not modify the original list.
        """
        print(sorted(self))
