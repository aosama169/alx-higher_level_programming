#!/usr/bin/python3
"""adds   new attribute to object
"""


def add_attribute(obj, attribute, value):
    """adds new attr """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
