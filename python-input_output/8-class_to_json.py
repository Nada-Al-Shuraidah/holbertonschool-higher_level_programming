#!/usr/bin/python3
"""Module that converts classinstances to dictionary for JSON serialization"""


def class_to_json(obj):
    """Return the dictionarydescription of an object for JSON serialization"""
    return obj.__dict__
