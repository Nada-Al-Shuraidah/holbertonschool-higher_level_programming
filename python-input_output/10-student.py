#!/usr/bin/python3
"""Module that defines a Student class with optional attribute filtering."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only return those attributes."""
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
