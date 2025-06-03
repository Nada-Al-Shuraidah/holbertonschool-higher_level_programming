#!/usr/bin/python3
"""Module that writes a string to a UTF-8 text file and returns char count."""


def write_file(filename="", text=""):
    """Writes a str to a text file(UTF8) & returns the num of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
