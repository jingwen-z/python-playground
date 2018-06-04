# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

DF = pd.DataFrame(np.arange(16).reshape(4, 4),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])


class TestLocIloc(unittest.TestCase):
    def test_slice_label(self):
        expected = pd.Series([1, 5, 9], index=['Ohio', 'Colorado', 'Utah'])
        expected.name = 'two'
        self.assertTrue((expected == DF.loc[:'Utah', 'two']).all())

    def test_single_col_loc(self):
        expected = pd.Series([1, 5, 9, 13],
                             index=['Ohio', 'Colorado', 'Utah', 'New York'])
        expected.name = 'two'
        self.assertTrue((expected == DF.loc[:, 'two']).all())

    def test_single_col_iloc(self):
        expected = pd.Series([1, 5, 9, 13],
                             index=['Ohio', 'Colorado', 'Utah', 'New York'])
        expected.name = 'two'
        self.assertTrue((expected == DF.iloc[:, 1]).all())

    def test_single_row_loc(self):
        expected = pd.Series([0, 1, 2, 3],
                             index=['one', 'two', 'three', 'four'])
        expected.name = 'Ohio'
        self.assertTrue((expected == DF.loc['Ohio']).all())

    def test_single_row_iloc(self):
        expected = pd.Series([0, 1, 2, 3],
                             index=['one', 'two', 'three', 'four'])
        expected.name = 'Ohio'
        self.assertTrue((expected == DF.iloc[0]).all())

    def test_scalar_val_label(self):
        self.assertTrue(
            (DF.at['Colorado', 'four'] == DF.loc['Colorado', 'four']).all())

    def test_scalar_val_pos(self):
        self.assertTrue(
            (DF.iat[1, 3] == DF.iloc[1, 3]).all())

    def test_reindex_col(self):
        expected = pd.DataFrame([0, 4, 8, 12], columns=['one'],
                                index=['Ohio', 'Colorado', 'Utah', 'New York'])
        pd.testing.assert_frame_equal(expected, DF.reindex(columns=['one']))

    def test_reindex_row(self):
        expected_df = pd.DataFrame([[0, 1, 2, 3]],
                                   columns=['one', 'two', 'three', 'four'],
                                   index=['Ohio'])
        pd.testing.assert_frame_equal(expected_df, DF.reindex(index=['Ohio']))

    def test_get_value(self):
        self.assertEqual(0, DF.get_value(index='Ohio', col='one'))

    def test_set_value(self):
        df2 = DF.copy()
        df2.set_value(index='Ohio', col='one', value=7)
        self.assertEqual(7, df2.get_value(index='Ohio', col='one'))


if __name__ == '__main__':
    unittest.main()
