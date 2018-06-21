#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
from numpy import nan as NA


class TestFilterOutMissingData(unittest.TestCase):
    def test_filter_na_series(self):
        data = pd.Series([1, NA, 3.5])
        self.assertTrue(
            (pd.Series([1, 3.5], index=[0, 2]) == data.dropna()).all())
        self.assertTrue((data.dropna() == data[data.notnull()]).all())

    def test_filter_na_df(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(pd.DataFrame([[1.0, 3.0, 3.6]]),
                                      data.dropna())

    def test_filter_na_all(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [NA, 7.2, 5]]),
            data.dropna(how='all'))

    def test_filter_na_thresh(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [NA, 7.2, 5]]),
            data.dropna(thresh=1))


class TestFillInMissingData(unittest.TestCase):
    def test_fillna(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [0, 7.2, 5], [0, 0, 0]]),
            data.fillna(0))

    def test_fillna_col(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [10, 7.2, 5], [10, 11, 12]]),
            data.fillna({0: 10, 1: 11, 2: 12}))

    def test_fillna_ffill(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [1.0, 7.2, 5], [NA, 7.2, 5.0]]),
            data.fillna(method='ffill', limit=1))

    def test_fillna_mean(self):
        data = pd.DataFrame([[1, 3, 3.6], [NA, 7.2, 5], [NA, NA, NA]])
        pd.testing.assert_frame_equal(
            pd.DataFrame([[1.0, 3.0, 3.6], [1.0, 7.2, 5], [1.0, 5.1, 4.3]]),
            data.fillna(data.mean()))


if __name__ == '__main__':
    unittest.main()
