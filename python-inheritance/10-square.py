#!/usr/bin/python3
"""Module defines a Square class inheriting from BaseGeometry."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """Square class inherits from BaseGeometry."""

    def __init__(self, size):
        """Initialize the square with size validated by integer_validator."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size**2

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
