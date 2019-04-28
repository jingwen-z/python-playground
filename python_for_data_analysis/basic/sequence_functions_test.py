#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest


class TestSequenceFunctions(unittest.TestCase):
    def test_enumerate(self):
        some_list = ['foo', 'bar', 'baz']
        mapping = {}

        for i, v in enumerate(some_list):
            mapping[v] = i

        self.assertEqual({'bar': 1, 'baz': 2, 'foo': 0}, mapping)

    def test_sorted(self):
        sorted_list = sorted([7, 1, 2, 6, 0, 3, 2])
        self.assertEqual([0, 1, 2, 2, 3, 6, 7], sorted_list)

        sorted_str = sorted('horse race')
        self.assertEqual([' ', 'a', 'c', 'e', 'e', 'h', 'o', 'r', 'r', 's'], sorted_str)

    def test_zip(self):
        seq1 = ['foo', 'bar', 'baz']
        seq2 = ['one', 'two', 'three']
        zipped = zip(seq1, seq2)
        self.assertEqual([('foo', 'one'), ('bar', 'two'), ('baz', 'three')], list(zipped))

        seq3 = [False, True]
        self.assertEqual([('foo', 'one', False), ('bar', 'two', True)], list(zip(seq1, seq2, seq3)))

    def test_zip_enumerate(self):
        seq1 = ['foo', 'bar', 'baz']
        seq2 = ['one', 'two', 'three']

        result = ''
        for i, (a, b) in enumerate(zip(seq1, seq2)):
            result += '{0}: {1}, {2}; '.format(i, a, b)
        self.assertEqual(result, '0: foo, one; 1: bar, two; 2: baz, three; ')

    def test_unzip(self):
        pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
        first_names, last_names = zip(*pitchers)

        self.assertEqual(('Nolan', 'Roger', 'Schilling'), first_names)
        self.assertEqual(('Ryan', 'Clemens', 'Curt'), last_names)

    def test_reversed(self):
        reversed_list = list(reversed(range(10)))
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], reversed_list)


if __name__ == '__main__':
    unittest.main()
