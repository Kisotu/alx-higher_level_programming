#!/usr/bin/python3
'''Unittests for Task 5'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Define unittests for max_integer([..]).'''

    def test_ordered_list(self):
        '''Test ordered list of integers.'''
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        '''Test unordered list of integers.'''
        unordered = [3, 4, 5, 6]
        self.assertEqual(max_integer(unordered), 6)

    def test_max_at_begginning(self):
        '''Test list with a beginning max value.'''
        max_at_beginning = [7, 6, 5, 4]
        self.assertEqual(max_integer(max_at_beginning), 7)

    def test_empty_list(self):
        '''Test empty list.'''
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        '''Test list with a single element.'''
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_floats(self):
        '''Test float list.'''
        floats = [2.67, 0.93, -7.156, 78.2, 7.8]
        self.assertEqual(max_integer(floats), 78.2)

    def test_ints_and_floats(self):
        '''Test list of ints/floats.'''
        ints_and_floats = [4.53, 65.7, -8, 23, 7]
        self.assertEqual(max_integer(ints_and_floats), 65.7)

    def test_string(self):
        '''Tests a string.'''
        string = "Kisotu"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        '''Tests list of strings.'''
        strings = ["This", "is", "a", "string", "list"]
        self.assertEqual(max_integer(strings), "string")

    def test_empty_string(self):
        '''Tests empty string.'''
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
