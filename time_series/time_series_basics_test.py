#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
from dateutil.parser import parse

DATES = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

TS = pd.Series(np.arange(1, 7), index=DATES)

LONGER_TS = pd.Series(np.arange(1000),
                      index=pd.date_range('2000-01-01', periods=1000))


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


if __name__ == '__main__':
    unittest.main()
