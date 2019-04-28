#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from collections import defaultdict


class TestDict(unittest.TestCase):
    def test_insert(self):
        d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
        d1[7] = 'an integer'
        self.assertEqual({'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}, d1)
        self.assertEqual([1, 2, 3, 4], d1['b'])
        self.assertEqual(True, 'b' in d1)

    def test_del(self):
        d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer', 5: 'some value', 'dummy': 'another value'}
        del d1[5]
        self.assertEqual({'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer', 'dummy': 'another value'}, d1)

        ret = d1.pop('dummy')
        self.assertEqual('another value', ret)
        self.assertEqual({'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}, d1)

    def test_pairs(self):
        d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
        self.assertEqual(['a', 'b', 7], list(d1.keys()))
        self.assertEqual(['some value', [1, 2, 3, 4], 'an integer'], list(d1.values()))

    def test_update(self):
        d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
        d1.update({'b': 'foo', 'c': 12})
        self.assertEqual({'a': 'some value', 'b': 'foo', 7: 'an integer', 'c': 12}, d1)

    def test_from_seq(self):
        mapping = dict(zip(range(5), reversed(range(5))))
        self.assertEqual({0: 4, 1: 3, 2: 2, 3: 1, 4: 0}, mapping)

    def test_iterate(self):
        words = ['apple', 'bat', 'bar', 'atom', 'book']
        by_letter = {}

        for word in words:
            key = word[0]
            if key in by_letter:
                by_letter[key].append(word)
            else:
                by_letter[key] = [word]
        self.assertEqual({'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}, by_letter)

    def test_get(self):
        words = ['apple', 'bat', 'bar', 'atom', 'book']
        by_letter = {}

        for word in words:
            key = word[0]

            value = by_letter.get(key, [])
            value.append(word)
            by_letter[key] = value
        self.assertEqual({'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}, by_letter)

    def test_setdefault(self):
        words = ['apple', 'bat', 'bar', 'atom', 'book']
        by_letter = {}

        for word in words:
            key = word[0]
            by_letter.setdefault(key, []).append(word)
        self.assertEqual({'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}, by_letter)

    def test_defaultdict(self):
        words = ['apple', 'bat', 'bar', 'atom', 'book']
        by_letter = defaultdict(list)
        for word in words:
            by_letter[word[0]].append(word)
        self.assertEqual({'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}, by_letter)

    def test_key_type(self):
        d = {}
        d[tuple([1, 2, 3])] = 5
        self.assertEqual({(1, 2, 3): 5}, d)


if __name__ == '__main__':
    unittest.main()
