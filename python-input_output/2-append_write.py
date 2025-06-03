#!/usr/bin/python3
"""Module that appends a string to a UTF-8 text file and returns char count."""


def append_write(filename="", text=""):
    """Appends a str to a text file(UTF8) & returns the num of chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
