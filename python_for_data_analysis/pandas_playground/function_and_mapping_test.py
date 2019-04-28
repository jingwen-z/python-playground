# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np

F = lambda x: x.max() - x.min()


class TestFunctionApplicationandMapping(unittest.TestCase):
    def test_apply_per_col(self):
        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['Ohio', 'Texas', 'Utah'],
                          columns=['a', 'b'])
        expected = pd.Series([4, 4], index=['a', 'b'])
        self.assertTrue((expected == df.apply(F)).all())

    def test_apply_per_row(self):
        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['Ohio', 'Texas', 'Utah'],
                          columns=['a', 'b'])
        expected = pd.Series([1, 1, 1], index=['Ohio', 'Texas', 'Utah'])
        self.assertTrue((expected == df.apply(F, axis='columns')).all())

    def test_return_series(self):
        def f(x):
            return pd.Series([x.min(), x.max()], index=['min', 'max'])

        df = pd.DataFrame(np.arange(6).reshape(3, 2),
                          index=['Ohio', 'Texas', 'Utah'],
                          columns=['a', 'b'])
        expected = pd.DataFrame({'a': [0, 4], 'b': [1, 5]},
                                index=['min', 'max'])

        pd.testing.assert_frame_equal(expected, df.apply(f))

    def test_elementwise(self):
        df = pd.DataFrame({'a': [0.4, 2.516, 1.3], 'b': [13.249, 5.23, 1.4254]},
                          index=['Ohio', 'Texas', 'Utah'],
                          columns=['a', 'b'])
        fmt = lambda x: '%.2f' % x
        expected = pd.DataFrame({'a': ['0.40', '2.52', '1.30'],
                                 'b': ['13.25', '5.23', '1.43']},
                                index=['Ohio', 'Texas', 'Utah'],
                                columns=['a', 'b'])

        pd.testing.assert_frame_equal(expected, df.applymap(fmt))

    def test_series_map(self):
        df = pd.DataFrame({'a': [0.4, 2.516, 1.3], 'b': [13.249, 5.23, 1.4254]},
                          index=['Ohio', 'Texas', 'Utah'],
                          columns=['a', 'b'])
        fmt = lambda x: '%.2f' % x
        ser = pd.Series(['0.40', '2.52', '1.30'],
                        index=['Ohio', 'Texas', 'Utah'])
        ser.name = 'a'

        self.assertTrue((ser == df['a'].map(fmt)).all())


if __name__ == '__main__':
    unittest.main()
