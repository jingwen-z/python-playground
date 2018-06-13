# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np

DF = pd.DataFrame(np.arange(6).reshape(3, 2),
                  index=['a', 'b', 'c'],
                  columns=['one', 'two'])


class TestDescriptiveStatistics(unittest.TestCase):
    def test_df_sum_col(self):
        expected = pd.Series([6, 9], index=['one', 'two'])
        self.assertTrue((expected == DF.sum()).all())

    def test_df_sum_row(self):
        expected = pd.Series([1, 5, 9], index=['a', 'b', 'c'])
        self.assertTrue((expected == DF.sum(axis='columns')).all())

    def test_idxmax(self):
        expected = pd.Series(['c', 'c'], index=['one', 'two'])
        self.assertTrue((expected == DF.idxmax()).all())

    def test_cumsum(self):
        expected = pd.DataFrame({'one': [0, 2, 6], 'two': [1, 4, 9]},
                                index=['a', 'b', 'c'],
                                columns=['one', 'two'])
        pd.testing.assert_frame_equal(expected, DF.cumsum())

    def test_describe_num_data(self):
        expected = pd.DataFrame(
            {'one': [3.0, 2.0, 2.0, 0.0, 1.0, 2.0, 3.0, 4.0],
             'two': [3.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 5.0]},
            index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'],
            columns=['one', 'two'])
        pd.testing.assert_frame_equal(expected, DF.describe())

    def test_describe_non_num_data(self):
        obj = pd.Series(['a', 'a', 'b'] * 2)
        expected = pd.Series([6, 2, 'a', 4],
                             index=['count', 'unique', 'top', 'freq'])
        self.assertTrue((expected == obj.describe()).all())

    def test_unique(self):
        obj = pd.Series(['c', 'c', 'b', 'b'])

        expected_unique = np.array(['c', 'b'])
        expected_val_count = pd.Series([2, 2],
                                       index=['b', 'c']).reset_index(drop=True)

        self.assertTrue((expected_unique == obj.unique()).all())
        self.assertTrue((expected_val_count == obj.value_counts().reset_index(
            drop=True)).all())

    def test_isin(self):
        obj = pd.Series(['c', 'c', 'b', 'a'])
        mask = obj.isin(['b', 'c'])
        expected = pd.Series([True, True, True, False])

        self.assertTrue((expected == mask).all())

    def test_df_value_counts(self):
        df = pd.DataFrame({'C1': [1, 1, 3],
                           'C2': [2, 6, 6],
                           'C3': [2, 3, 7]})
        result = df.apply(pd.value_counts).fillna(0)

        expected = pd.DataFrame({'C1': [2.0, 0.0, 1.0, 0.0, 0.0],
                                 'C2': [0.0, 1.0, 0.0, 2.0, 0.0],
                                 'C3': [0.0, 1.0, 1.0, 0.0, 1.0]},
                                index=[1, 2, 3, 6, 7])

        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
