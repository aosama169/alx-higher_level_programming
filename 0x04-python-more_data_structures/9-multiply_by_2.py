#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    directory = a_dictionary.copy()
    list_keys = list(directory.keys())

    for i in list_keys:
        directory[i] *= 2

    return (directory)
