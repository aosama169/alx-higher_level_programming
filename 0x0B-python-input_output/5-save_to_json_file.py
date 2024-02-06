#!/usr/bin/python3
""" Module that writes Object to a text file using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes object to text file
    by a JSON

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object cannott be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
