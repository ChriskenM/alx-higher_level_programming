#!/usr/bin/python3

"""
Defines baseshape class.
"""


class BaseGeometry:
    """ Empty class """
    def area(self):
        raise Exception("area() is not implemented")
