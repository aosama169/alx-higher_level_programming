#!/usr/bin/python3
""" Module that contains function writes to a text file
"""


def write_file(filename="", text=""):
    """ Function writes to text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file cannot be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
