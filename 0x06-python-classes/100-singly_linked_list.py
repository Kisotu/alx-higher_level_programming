#!/usr/bin/python3
'''task 100 - define classes for a singly-linked list.'''


class Node:
    '''class Node for a node in a singly-linked list.'''

    def __init__(self, data, next_node=None):
        '''initialize new Node.

        Args:
            data (int): The data of new Node.
            next_node (Node): The next node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''get the data of the Node.'''
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''get the next_node of the Node.'''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' Class for a singly-linked list.'''

    def __init__(self):
        '''init a new SinglyLinkedList.'''
        self.__head = None

    def sorted_insert(self, value):
        '''inserts new Node to the SinglyLinkedList.

        node is inserted into the list at the correct
        order

        Args:
            value (Node): The Node to insert.
        '''
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
        '''define print() representation of a SinglyLinkedList.'''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
