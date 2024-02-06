#!/usr/bin/python3
""" Module that contains function appends to text file
"""


def append_write(filename="", text=""):
    """ Function appends to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when file cannot be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
