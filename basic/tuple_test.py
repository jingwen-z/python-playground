#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


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
        self.assertEqual(('foo', [1, 2, 3], True), tup_new)

    def test_tuple_plus(self):
        tup = (4, None, 'foo') + (6, 0) + ('bar',)
        self.assertEqual((4, None, 'foo', 6, 0, 'bar'), tup)

    def test_tuple_multiply(self):
        tup = ('foo', 'bar') * 4
        self.assertEqual(('foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'), tup)


class TestUnpackingTuple(unittest.TestCase):
    def test_simple_unpack(self):
        tup = (4, 5, 6)
        a, b, c = tup
        self.assertEqual(5, b)

    def test_nested_unpack(self):
        tup = 4, 5, (6, 7)
        a, b, (c, d) = tup
        self.assertEqual(7, d)

    def test_swap(self):
        a, b = 1, 2
        b, a = a, b
        self.assertEqual(2, a)
        self.assertEqual(1, b)

    def test_unpack_iter(self):
        seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        for a, b, c in seq:
            print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
        self.assertEqual(7, a)

    def test_rest(self):
        values = 1, 2, 3, 4, 5
        a, b, *rest = values
        a, b, *_ = values

        self.assertEqual(1, a)
        self.assertEqual([3, 4, 5], rest)
        self.assertEqual([3, 4, 5], _)

    def test_tuple_count(self):
        a = (1, 2, 2, 2, 3, 4, 2)
        self.assertEqual(4, a.count(2))
