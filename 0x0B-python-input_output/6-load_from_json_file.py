#!/usr/bin/python3
""" Module that creates Object from JSON
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from JSON

    Args:
        filename: text file name

    Raises:
        Exception: when the object cannot be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
