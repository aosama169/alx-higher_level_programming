#!/usr/bin/python3
"""Find peak in list of unsorted int"""


def find_peak(list_of_integers):
    """Find peak in list_of_int"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lowInt = 0
    hi = len(list_of_integers)
    mediums = ((hi - lowInt) // 2) + lowInt
    mediums = int(mediums)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mediums] >= list_of_integers[mediums - 1] and\
            list_of_integers[mediums] >= list_of_integers[mediums + 1]:
        return list_of_integers[mediums]
    if mediums > 0 and list_of_integers[mediums] < list_of_integers[mediums + 1]:
        return find_peak(list_of_integers[mediums:])
    if mediums > 0 and list_of_integers[mediums] < list_of_integers[mediums - 1]:
        return find_peak(list_of_integers[:mediums])
