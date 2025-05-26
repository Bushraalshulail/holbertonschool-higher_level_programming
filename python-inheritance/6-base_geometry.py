#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class intended for geometry operations.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not yet implemented.
        """
        raise Exception("area() is not implemented")
