#!/usr/bin/python3
""" Module that contains function that returns object by a JSON
"""
import json


def from_json_string(my_str):
    """ Function that returns object by JSON

    Args:
        my_str: JSON

    Raises:
        Exception: when the string cannot be decoded

    """
    return json.loads(my_str)
