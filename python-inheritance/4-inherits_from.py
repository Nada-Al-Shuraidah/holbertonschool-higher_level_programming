#!/usr/bin/python3
"""
Module that defines inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class
    (directly or indirectly). Otherwise, returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
