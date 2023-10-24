#!/usr/bin/python3
"""Define MagicClass matching exactly the bytecode provided"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference."""
        return (2 * math.pi * self.__radius)
