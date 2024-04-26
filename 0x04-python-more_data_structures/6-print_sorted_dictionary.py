#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listOrded = list(a_dictionary.keys())
    listOrded.sort()
    for i in listOrded:
        print("{}: {}".format(i, a_dictionary.get(i)))
