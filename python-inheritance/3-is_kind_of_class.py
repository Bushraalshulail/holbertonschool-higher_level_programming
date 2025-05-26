#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of,
or an instance of a class that inherited from,
a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an inst of a_class or inherits from it;else False.
    """
    return isinstance(obj, a_class)
