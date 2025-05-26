#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
It includes a method to print the list sorted in ascending order,
handling positive and negative integers correctly.
"""


class MyList(list):
    """
    MyList is a subclass of list with an added method to
    print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order.
        The original list remains unmodified.
        """
        # Use sorted() which handles negative and positive numbers naturally
        sorted_list = sorted(self)
        print(sorted_list)
