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
        self.assertEqual('s', str_tup[0])


class TestTupleList(unittest.TestCase):
    def test_tuple_append(self):
        tup = tuple(['foo', [1, 2], True])
        tup[1].append(3)
        tup_new = tuple(tup)
        self.assertEqual(tuple(['foo', [1, 2, 3], True]), tup_new)

    def test_tuple_plus(self):
        tup=(4, None, 'foo') +


if __name__ == '__main__':
    unittest.main()
