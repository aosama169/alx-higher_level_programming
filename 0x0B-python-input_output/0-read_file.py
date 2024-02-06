#!/usr/bin/python3
""" Module that contains function that reads from file """


def read_file(filename=""):
    """ Function that reads from file

    Args:
        filename: filename

    Raises
        Exception: when file cannot be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
