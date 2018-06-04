# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np


class TestDrop(unittest.TestCase):
    def test_series_drop(self):
        obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
        obj2 = obj.drop('d')
        self.assertTrue(
            (pd.Series([0, 1, 2, 4], index=['a', 'b', 'c', 'e']) == obj2).all())

    def test_df_row_drop(self):
        df = pd.DataFrame(np.arange(9).reshape(3, 3),
                          index=['R1', 'R2', 'R3'],
                          columns=['C1', 'C2', 'C3'])
        df.drop(['R1', 'R3'], inplace=True)

        self.assertTrue('R2' == df.index)
        self.assertFalse('R1' in df.index)

    def test_df_col_drop(self):
        df = pd.DataFrame(np.arange(9).reshape(3, 3),
                          index=['R1', 'R2', 'R3'],
                          columns=['C1', 'C2', 'C3'])
        df.drop(['C2', 'C3'], axis=1, inplace=True)
        self.assertTrue('C1' == df.columns)
        self.assertFalse('C2' in df.columns)


if __name__ == '__main__':
    unittest.main()
