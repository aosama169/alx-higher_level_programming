#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listKey = list(a_dictionary.keys())

    for valueKey in listKey:
        if value == a_dictionary.get(valueKey):
            del a_dictionary[valueKey]

    return (a_dictionary)
