# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np
import math


class TestArithmetic(unittest.TestCase):
    def test_series(self):
        s1 = pd.Series([3, -1, 4], index=['a', 'b', 'd'])
        s2 = pd.Series([2, -5, 0], index=['b', 'c', 'd'])
        stotal = s1 + s2
        self.assertTrue(math.isnan(stotal[0]))
        self.assertFalse(math.isnan(stotal[1]))

    def test_df(self):
        df1 = pd.DataFrame(np.arange(4).reshape(2, 2),
                           index=['a', 'b'], columns=list('bc'))
        df2 = pd.DataFrame(np.arange(6).reshape(3, 2),
                           index=['b', 'c', 'd'], columns=list('ab'))
        dftotal = df1 + df2
        self.assertTrue(math.isnan(dftotal.loc['a', 'c']))
        self.assertFalse(math.isnan(dftotal.loc['b', 'b']))
        self.assertEqual(3, dftotal.loc['b', 'b'])


if __name__ == '__main__':
    unittest.main()
