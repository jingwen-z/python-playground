# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np


class TestSortingRanking(unittest.TestCase):
    def test_sort_index_row(self):
        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['two', 'three', 'one'],
                          columns=['b', 'a'])
        expected = pd.DataFrame({'b': [4, 2, 0], 'a': [5, 3, 1]},
                                index=['one', 'three', 'two'],
                                columns=['b', 'a'])

        pd.testing.assert_frame_equal(expected, df.sort_index())

    def test_sort_index_col(self):
        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['two', 'three', 'one'],
                          columns=['b', 'a'])
        expected = pd.DataFrame({'a': [1, 3, 5], 'b': [0, 2, 4]},
                                index=['two', 'three', 'one'])

        pd.testing.assert_frame_equal(expected, df.sort_index(axis=1))

    def test_sort_multi_values(self):
        df = pd.DataFrame({'b': [4, 2, 3], 'a': [5, 3, 1], 'c': [2, 1, 3]},
                          index=['two', 'one', 'three'],
                          columns=['b', 'a', 'c'])
        expected = pd.DataFrame({'b': [3, 2, 4], 'a': [1, 3, 5],
                                 'c': [3, 1, 2]},
                                index=['three', 'one', 'two'],
                                columns=['b', 'a', 'c'])

        pd.testing.assert_frame_equal(expected, df.sort_values(by=['a', 'b']))
        pd.testing.assert_frame_equal(df.sort_values(by='a'),
                                      df.sort_values(by=['a', 'b']))

    def test_rank_series_first(self):
        ser = pd.Series([7, -1, 3, 7, 0, 3])
        expected = pd.Series([5.0, 1.0, 3.0, 6.0, 2.0, 4.0])
        self.assertTrue((expected == ser.rank(method='first')).all())

    def test_rank_series_desc(self):
        ser = pd.Series([7, -1, 3, 7, 0, 3])
        expected = pd.Series([1.0, 6.0, 3.0, 1.0, 5.0, 3.0])
        self.assertTrue(
            (expected == ser.rank(ascending=False, method='min')).all())

    def test_df_rank_col(self):
        df = pd.DataFrame({'b': [4, 2, 3], 'a': [5, 3, 1], 'c': [2, 7, 3]},
                          index=['two', 'one', 'three'],
                          columns=['b', 'a', 'c'])
        expected = pd.DataFrame(
            {'b': [2.0, 1.0, 2.0], 'a': [3.0, 2.0, 1.0], 'c': [1.0, 3.0, 2.0]},
            index=['two', 'one', 'three'],
            columns=['b', 'a', 'c'])

        pd.testing.assert_frame_equal(expected,
                                      df.rank(axis='columns', method='min'))


if __name__ == '__main__':
    unittest.main()
