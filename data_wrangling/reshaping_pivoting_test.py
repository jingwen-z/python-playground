#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd
from numpy import nan as NA

DATA = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))


class TestReshapingwithHierarchicalIndexing(unittest.TestCase):
    def test_stack(self):
        result = DATA.stack().unstack()
        pd.testing.assert_frame_equal(DATA, result)


class TestPivotingLongWideFormat(unittest.TestCase):
    def test_pivoting_long_to_wide(self):
        long_df = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo', 'bar',
                                        'baz', 'foo', 'bar', 'baz'],
                                'variable': ['A', 'A', 'A', 'B', 'B',
                                             'B', 'C', 'C', 'C'],
                                'value': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
        expected = pd.DataFrame({'A': [2, 3, 1], 'B': [5, 6, 4],
                                 'C': [8, 9, 7]}, index=['bar', 'baz', 'foo'])
        expected.index.name = 'key'
        expected.columns.name = 'variable'
        pd.testing.assert_frame_equal(long_df.pivot('key', 'variable', 'value'),
                                      expected)

    def test_pivoting_wide_to_long(self):
        wide_df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                                'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo', 'bar',
                                         'baz', 'foo', 'bar', 'baz'],
                                 'variable': ['A', 'A', 'A', 'B', 'B',
                                              'B', 'C', 'C', 'C'],
                                 'value': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
                                columns=['key', 'variable', 'value'])
        pd.testing.assert_frame_equal(pd.melt(wide_df, ['key']),
                                      expected)


if __name__ == '__main__':
    unittest.main()
