#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area of shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of shape."""
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (Duck Typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
