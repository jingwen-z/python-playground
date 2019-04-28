#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
from numpy import nan as NA

MULTI_DIM_SER = pd.Series([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                          index=[['a', 'a', 'a', 'b', 'b', 'c', 'c'],
                                 [1, 2, 3, 1, 3, 1, 2]])


class TestHierarcicalIndexing(unittest.TestCase):
    def test_unstack(self):
        unstacked = pd.DataFrame(
            {1: [0.0, 3.0, 5.0], 2: [1, NA, 6], 3: [2, 4, NA]},
            columns=[1, 2, 3], index=['a', 'b', 'c'])
        pd.testing.assert_frame_equal(unstacked, MULTI_DIM_SER.unstack())

    def test_stack(self):
        pd.testing.assert_series_equal(MULTI_DIM_SER,
                                       MULTI_DIM_SER.unstack().stack())


class TestIndexwithDFColumns(unittest.TestCase):
    def test_set_index(self):
        df = pd.DataFrame({'a': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                           'b': [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0],
                           'c': ['a', 'a', 'a', 'b', 'b', 'b', 'b'],
                           'd': [2, 6, 7, 8, 6, 9, 1]})

        expected = pd.DataFrame({'a': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                                 'b': [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]},
                                index=[['a', 'a', 'a', 'b', 'b', 'b', 'b'],
                                       [2, 6, 7, 8, 6, 9, 1]])
        expected.index.names = ['c', 'd']

        pd.testing.assert_frame_equal(expected, df.set_index(['c', 'd']))


if __name__ == '__main__':
    unittest.main()
