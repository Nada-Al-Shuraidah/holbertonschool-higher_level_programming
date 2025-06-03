#!/usr/bin/python3
"""Module that reads and prints the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
