#!/usr/bin/python3
"""unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.testcase):
    '''Define unittests for max_integer([..]).'''

    def test_ordered_list(self):
        '''test list of int'''
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        '''test unordered list of int'''
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        '''test max value at beginning of list'''
        max_at_begining = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begining), 4)

    def test_empty_lists(self):
        '''test an empty list'''
        empty = []
        self.assertEqual(max_integer(empty),None)

    def test_one_element_list(self):
        '''test a list with single element'''
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        '''test using floats'''
        floats = [1.53, 6.33, -9.54, 15.5, 6.72]
        self.assertEqual(max_integer(floats), 15.5)

    def test_int_and_floats_list(self):
        '''test for int and floats'''
        int_and_floats = [1.53, 15.2, -9, 14, 6]
        self.assertEqual(max_integer(int_and_floats), 15.2)

    def test_string(self):
        '''test a list of string'''
        string = "greatness"
        self.assertEqual(max_integer(string), "t")

    def test_list_of_strings(self):
        '''Teting a list of string'''
        list_of_strings = ['God' 'is' 'great']
        self.assertEqual(max_integer(list_of_strings), "God")

    def test_empty_string(self):
        '''testing an empty string'''
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
