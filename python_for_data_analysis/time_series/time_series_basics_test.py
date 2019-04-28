#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

import numpy as np
import pandas as pd

DATES = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

TS = pd.Series(np.arange(1, 7), index=DATES)

LONGER_TS = pd.Series(np.arange(1000),
                      index=pd.date_range('2000-01-01', periods=1000))

DUP_TS = pd.Series(np.arange(5),
                   index=pd.DatetimeIndex(
                       ['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000',
                        '1/3/2000']))


class TestIndexingSelectionSubsetting(unittest.TestCase):
    def test_index(self):
        self.assertEqual(LONGER_TS[LONGER_TS.index[1]], 1)
        self.assertEqual(LONGER_TS['1/2/2000'], 1)
        self.assertEqual(LONGER_TS['1/2/2000'], LONGER_TS['20000102'])

    def test_index_str_year(self):
        self.assertEqual(len(LONGER_TS['2001']), 365)
        self.assertEqual(LONGER_TS['2001'][0], 365 + 1)
        self.assertEqual(LONGER_TS['2001'][len(LONGER_TS['2001']) - 1], 365 * 2)
        self.assertEqual(
            LONGER_TS['2001'][len(LONGER_TS['2001']) - 1] -
            LONGER_TS['2001'][0] + 1, 365)

    def test_index_str_month(self):
        self.assertEqual(len(LONGER_TS['2001-05']), 31)
        self.assertEqual(
            LONGER_TS['2001-05'][len(LONGER_TS['2001-05']) - 1] -
            LONGER_TS['2001-05'][0] + 1, 31)

    def test_index_datetime(self):
        self.assertTrue((TS[datetime(2011, 1, 10):] ==
                         pd.Series([5, 6],
                                   index=[datetime(2011, 1, 10),
                                          datetime(2011, 1, 12)])).all())

        self.assertTrue((TS['1/6/2011':'1/10/2011'] ==
                         pd.Series([3, 4, 5], index=[datetime(2011, 1, 7),
                                                     datetime(2011, 1, 8),
                                                     datetime(2011, 1,
                                                              10)])).all())

    def test_truncate(self):
        self.assertTrue((TS.truncate(before='1/7/2011') ==
                         pd.Series([3, 4, 5, 6], index=[datetime(2011, 1, 7),
                                                        datetime(2011, 1, 8),
                                                        datetime(2011, 1, 10),
                                                        datetime(2011, 1,
                                                                 12)])).all())
        self.assertTrue((TS.truncate(after='1/7/2011') ==
                         pd.Series([1, 2, 3], index=[datetime(2011, 1, 2),
                                                     datetime(2011, 1, 5),
                                                     datetime(2011, 1,
                                                              7)])).all())


class TestTSwithDuplicatsIdx(unittest.TestCase):
    def test_is_unique(self):
        self.assertFalse(DUP_TS.index.is_unique)


if __name__ == '__main__':
    unittest.main()
