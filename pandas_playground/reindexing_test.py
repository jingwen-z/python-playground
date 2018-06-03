# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd


class TestReindex(unittest.TestCase):
    def test_reindex(self):
        obj = pd.Series([2, 4, 1, 3], index=['b', 'd', 'a', 'c'])
        obj2 = obj.reindex(['a', 'b', 'c', 'd'])
        self.assertTrue((['a', 'b', 'c', 'd'] == obj2.index).all())
        self.assertTrue(
            (pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']) == obj2).all())

    def test_method(self):
        obj = pd.Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
        obj2 = obj.reindex(range(7), method='ffill')
        self.assertTrue((pd.Series(
            ['blue', 'blue', 'red', 'red', 'yellow', 'yellow', 'yellow'],
            index=range(7)) == obj2).all())


if __name__ == '__main__':
    unittest.main()
