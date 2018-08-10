#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd
from numpy import nan as NA

LEFT = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'c'],
                     'value': range(5)})
RIGHT = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

S1 = pd.Series([0, 1], index=['a', 'b'])
S2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
S3 = pd.Series([5, 6], index=['f', 'g'])


class TestMergingOnIndex(unittest.TestCase):
    def test_right_index(self):
        merged = pd.merge(LEFT, RIGHT, left_on='key', right_index=True)
        expected = pd.DataFrame({'key': ['a', 'a', 'b', 'b'],
                                 'value': [0, 2, 1, 3, ],
                                 'group_val': [3.5, 3.5, 7, 7]},
                                columns=['key', 'value', 'group_val'],
                                index=[0, 2, 1, 3])
        pd.testing.assert_frame_equal(merged, expected)

    def test_merge_hierarchical_indes(self):
        lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                                       'Nevada', 'Nevada'],
                              'key2': [2000, 2001, 2002, 2001, 2002],
                              'data': np.arange(5.)})
        righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                              index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                                      'Ohio', 'Ohio'],
                                     [2001, 2000, 2000, 2000, 2001, 2002]],
                              columns=['event1', 'event2'])
        merged = pd.merge(lefth, righth, left_on=['key1', 'key2'],
                          right_index=True)

        expected = pd.DataFrame({'data': [0.0, 0.0, 1.0, 2.0, 3.0],
                                 'key1': ['Ohio', 'Ohio', 'Ohio', 'Ohio',
                                          'Nevada'],
                                 'key2': [2000, 2000, 2001, 2002, 2001],
                                 'event1': [4, 6, 8, 10, 0],
                                 'event2': [5, 7, 9, 11, 1]},
                                columns=['data', 'key1', 'key2',
                                         'event1', 'event2'],
                                index=[0, 0, 1, 2, 3])

        pd.testing.assert_frame_equal(merged, expected)

    def test_join(self):
        merged = LEFT.join(RIGHT, on='key')
        expected = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'c'],
                                 'value': [0, 1, 2, 3, 4],
                                 'group_val': [3.5, 7.0, 3.5, 7.0, NA]},
                                columns=['key', 'value', 'group_val'])
        pd.testing.assert_frame_equal(merged, expected)


class TestConcatenating(unittest.TestCase):
    def test_numpy_concatenate(self):
        arr = np.arange(6).reshape((3, 2))
        concatenated = np.concatenate([arr, arr], axis=1)
        expected = np.array([[0, 1, 0, 1], [2, 3, 2, 3], [4, 5, 4, 5]])

        self.assertTrue((concatenated == expected).all())

    def test_pandas_concat(self):



if __name__ == '__main__':
    unittest.main()
