#!/usr/bin/python3
"""Define classes for a singly-linked list"""


class Node:
    """Represent a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): data of new Node
            next_node (Node): next node of new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data of Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set next_node of Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list"""

    def __init__(self):
        """Initalize a new Singly Linked List"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node to Singly Linked List

        node is inserted into list at correct ordered num pos

        Args:
            value (Node): new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define print() representation of a Single Linked List"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
