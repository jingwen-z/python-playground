#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import unittest


class TestFunctions(unittest.TestCase):
    def test_lambda(self):
        strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
        strings.sort(key=lambda x: len(set(list(x))))

        self.assertEqual(['aaaa', 'foo', 'abab', 'bar', 'card'], strings)

    def test_generator(self):
        gen_1 = sum(x ** 2 for x in range(100))
        self.assertEqual(328350, gen_1)

        gen_2 = dict((i, i ** 2) for i in range(5))
        self.assertEqual({0: 0, 1: 1, 2: 4, 3: 9, 4: 16}, gen_2)

    def test_itertools_groupby(self):
        first_letter = lambda x: x[0]
        names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
        by_letter = {}

        for letter, names in itertools.groupby(names, first_letter):
            by_letter[letter] = list(names)

        self.assertEqual({'A': ['Albert'], 'W': ['Wes', 'Will'], 'S': ['Steven']}, by_letter)


if __name__ == '__main__':
    unittest.main()
