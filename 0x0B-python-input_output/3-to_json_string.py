#!/usr/bin/python3
""" Module contains function return JSON of an object
"""
import json


def to_json_string(my_obj):
    """ Function returns JSON of an object
    Args:
        my_obj: object
    Raises:
        Exception: when object cannot be encoded
    """
    return json.dumps(my_obj)
