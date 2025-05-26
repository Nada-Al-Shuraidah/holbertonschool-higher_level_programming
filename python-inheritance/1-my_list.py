#!/usr/bin/python3
"""Module that defines a subclass of list with a sorted print method."""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.

    It adds a method that prints the list in sorted (ascending) order
    without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
