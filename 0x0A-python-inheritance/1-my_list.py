#!/usr/bin/python3
"""class MyList inherit from list
"""


class MyList(list):
    """inherit from list"""
    def print_sorted(self):
        """prints the sorted list
        """
        print(sorted(self))
