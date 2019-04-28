# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

SER = pd.Series(np.arange(3))


class TestLocIloc(unittest.TestCase):
    def test_slice(self):
        expected = pd.Series([0])
        self.assertTrue((expected == SER[:1]).all())

    def test_int_index_loc(self):
        expected = pd.Series([0, 1])
        self.assertTrue((expected == SER.loc[:1]).all())

    def test_int_index_iloc(self):
        expected = pd.Series([0])
        self.assertTrue((expected == SER.iloc[:1]).all())


if __name__ == '__main__':
    unittest.main()
