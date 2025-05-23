#!/usr/bin/python3
"""Defines a class Square with position-aware printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' and respecting position."""
        if self.__size == 0:
            print()
            return

        # Vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each line with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
