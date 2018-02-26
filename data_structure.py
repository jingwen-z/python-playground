#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

"""
Chapter 3: Built-in data structures, functions, and files

3.1 Data structures and sequences
"""


class TestTuple(unittest.TestCase):
    def test_tuple(self):
        tup = 4, 5, 6
        self.assertEqual((4, 5, 6), tup)

    def test_nested_tuple(self):
        nested_tup = (4, 5, 6), (7, 8)
        self.assertEqual(((4, 5, 6), (7, 8)), nested_tup)

    def test_tuple_str(self):
        str_tup = tuple('string')
        self.assertEqual(('s', 't', 'r', 'i', 'n', 'g'), str_tup)


if __name__ == '__main__':
    unittest.main()
