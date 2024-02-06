#!/usr/bin/python3
""" Module return dictionary desc with simple data structure for JSON
"""


def class_to_json(obj):
    """ Function that retun dictionary desc of obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
