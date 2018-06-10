# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np


class TestIndexWithDuplicateLabels(unittest.TestCase):
    def test_is_unique(self):
        obj = pd.Series(range(5), index=['a', 'b', 'c', 'b', 'a'])
        self.assertFalse(obj.index.is_unique)

    def test_series_duplicate_labels(self):
        obj = pd.Series(range(5), index=['a', 'b', 'c', 'b', 'a'])
        self.assertTrue((obj['a'] == pd.Series([0, 4], index=['a', 'a'])).all())
        self.assertEqual(2, obj['c'])

    def test_df_duplicate_labels(self):
        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['a', 'a', 'b'], columns=['c1', 'c2'])
        expected = pd.DataFrame(np.arange(4).reshape(2, 2),
                                index=['a', 'a'], columns=['c1', 'c2'])
        pd.testing.assert_frame_equal(expected, df.loc['a'])


if __name__ == '__main__':
    unittest.main()
