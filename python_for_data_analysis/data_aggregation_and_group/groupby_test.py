#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

PEOPLE = pd.DataFrame(np.arange(25).reshape(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
MAPPING = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}


class TestGroupby(unittest.TestCase):
    def test_group_with_dict(self):
        by_dict = PEOPLE.groupby(MAPPING, axis='columns').sum()
        expected = pd.DataFrame({'blue': [5, 15, 25, 35, 45],
                                 'red': [5, 20, 35, 50, 65]},
                                index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
        pd.testing.assert_frame_equal(expected, by_dict)

    def test_goroup_with_series(self):
        by_series = PEOPLE.groupby(pd.Series(MAPPING), axis='columns').count()
        expected = pd.DataFrame({'blue': [2] * 5, 'red': [3] * 5},
                                index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
        pd.testing.assert_frame_equal(expected, by_series)

    def test_group_with_fuctions(self):
        by_functions = PEOPLE.groupby(len).sum()
        self.assertEqual(by_functions.loc[3, 'e'],
                         PEOPLE.loc['Joe', 'e'] + PEOPLE.loc['Wes', 'e'] +
                         PEOPLE.loc['Jim', 'e'])

    def test_by_index_levels(self):
        multi_idx = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                               [1, 3, 5, 1, 3]],
                                              names=['cty', 'tenor'])
        multi_idx_df = pd.DataFrame(np.arange(20).reshape(4, 5),
                                    columns=multi_idx)
        by_idx_levels = multi_idx_df.groupby(level='cty',
                                             axis='columns').count()
        expected = pd.DataFrame({'JP': [2] * 4, 'US': [3] * 4},
                                columns=['JP', 'US'])
        expected.columns.name = 'cty'
        pd.testing.assert_frame_equal(expected, by_idx_levels)


if __name__ == '__main__':
    unittest.main()
