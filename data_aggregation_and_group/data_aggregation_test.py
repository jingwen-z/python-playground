#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

DF = pd.DataFrame({'total_bill': [10, 40, 20, 21, 19],
                   'tip': [1, 3, 2, 1.4, 1.9],
                   'smoker': ['No'] * 5, 'day': ['Sun'] * 5,
                   'time': ['Dinner'] * 5,
                   'size': [2, 3, 4, 3, 2],
                   'tip_pct': [0.1, 0.075, 0.1, 0.07, 0.1]})


class TestDataAggregation(unittest.TestCase):
    def test_multi_functions(self):
        print(DF)


if __name__ == '__main__':
    unittest.main()
