#!/usr/bin/python3
"""
This module defines a Square class that allows
comparison operations based on square area.
"""


class Square:
    """
    Represents a square with support for size validation
    and comparison by area.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        Args:
            size (int or float): Size of the square's side.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        Args:
            value (int or float): The size to set.
        Raises:
            TypeError: If value is not a number.
            ValueError: If value is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison based on area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Non-equality comparison based on area.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less-than comparison based on area.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less-than-or-equal comparison based on area.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater-than comparison based on area.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater-than-or-equal comparison based on area.
        """
        return self.area() >= other.area()
