#!/usr/bin/python3
""" class My Int that inherits from integer :
"""


class MyInt(int):
    """ empty Class """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
