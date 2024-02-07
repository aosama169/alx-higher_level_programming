#!/usr/bin/python3
""" Module defines class Student
"""


class Student:
    """ Class to create student instance """

    def __init__(self, first_name, last_name, age):
        """ Special method to init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method return directory """
        return self.__dict__.copy()
