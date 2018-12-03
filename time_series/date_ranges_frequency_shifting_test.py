# -*- coding: utf-8 -*-

import math
import unittest
from datetime import datetime

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd

DATES = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

TS = pd.Series(np.arange(1, 7), index=DATES)
FREQ_TS = pd.Series(np.arange(4),
                    index=pd.date_range('1/1/2000', periods=4, freq='M'))


class TestGenerateDateRanges(unittest.TestCase):
    def test_date_range_basic(self):
        self.assertTrue(
            (pd.date_range('2012-04-01', '2012-04-10') == pd.DatetimeIndex(
                ['2012-04-01', '2012-04-02', '2012-04-03', '2012-04-04',
                 '2012-04-05', '2012-04-06', '2012-04-07', '2012-04-08',
                 '2012-04-09', '2012-04-10'])).all())
        self.assertTrue(
            (pd.date_range(start='2012-04-01', periods=10) == pd.DatetimeIndex(
                ['2012-04-01', '2012-04-02', '2012-04-03', '2012-04-04',
                 '2012-04-05', '2012-04-06', '2012-04-07', '2012-04-08',
                 '2012-04-09', '2012-04-10'])).all())

    def test_date_range_with_time(self):
        result = pd.date_range('2011-01-01 12:12:12', periods=3)
        self.assertTrue((result ==
                         pd.DatetimeIndex(['2011-01-01 12:12:12',
                                           '2011-01-02 12:12:12',
                                           '2011-01-03 12:12:12'])).all())

    def test_normalize_timestamps(self):
        result = pd.date_range('2011-01-01 12:12:12', periods=3, normalize=True)
        self.assertTrue((result ==
                         pd.DatetimeIndex(['2011-01-01', '2011-01-02',
                                           '2011-01-03'])).all())


class TestFrequencyDateOffsets(unittest.TestCase):
    def test_simple_offset(self):
        expected = pd.DatetimeIndex(
            ['2000-01-01 00:00:00', '2000-01-01 06:00:00',
             '2000-01-01 12:00:00', '2000-01-01 18:00:00',
             '2000-01-02 00:00:00'])
        self.assertTrue((expected == pd.date_range('2000-01-01', '2000-01-02',
                                                   freq='6h')).all())
        self.assertTrue((pd.date_range('2000-01-01', '2000-01-02', freq='6h') ==
                         pd.date_range('2000-01-01', '2000-01-02',
                                       freq=Hour(6))).all())

    def test_combined_offset(self):
        expected = pd.DatetimeIndex(
            ['2000-01-01 00:00:00', '2000-01-01 06:30:00',
             '2000-01-01 13:00:00', '2000-01-01 19:30:00'])
        self.assertTrue((expected == pd.date_range('2000-01-01', '2000-01-02',
                                                   freq='6h30min')).all())
        self.assertTrue((pd.date_range('2000-01-01', '2000-01-02',
                                       freq='6h30min') ==
                         pd.date_range('2000-01-01', '2000-01-02',
                                       freq=Hour(6) + Minute(30))).all())

    def test_week_of_month(self):
        third_fris = pd.date_range('2012-01-01', '2012-05-01', freq='WOM-3FRI')
        self.assertTrue((third_fris ==
                         pd.DatetimeIndex(['2012-01-20', '2012-02-17',
                                           '2012-03-16', '2012-04-20'])).all())
        self.assertEqual(list(third_fris),
                         [pd.Timestamp('2012-01-20 00:00:00'),
                          pd.Timestamp('2012-02-17 00:00:00'),
                          pd.Timestamp('2012-03-16 00:00:00'),
                          pd.Timestamp('2012-04-20 00:00:00')])


class TestShiftingData(unittest.TestCase):
    def test_basic_shifting(self):
        pd.testing.assert_series_equal(FREQ_TS.shift(2),
                                       pd.Series([math.nan, math.nan, 0, 1],
                                                 index=pd.date_range('1/1/2000',
                                                                     periods=4,
                                                                     freq='M')))
        pd.testing.assert_series_equal(FREQ_TS.shift(-2),
                                       pd.Series([2, 3, math.nan, math.nan],
                                                 index=pd.date_range('1/1/2000',
                                                                     periods=4,
                                                                     freq='M')))

    def test_shift_month(self):
        pd.testing.assert_series_equal(FREQ_TS.shift(2, freq='M'),
                                       pd.Series(np.arange(4),
                                                 index=pd.date_range('3/1/2000',
                                                                     periods=4,
                                                                     freq='M')))

    def test_shift_minute(self):
        pd.testing.assert_series_equal(FREQ_TS.shift(1, freq='90T'),
                                       pd.Series(np.arange(4),
                                                 index=pd.date_range(
                                                     '1/31/2000 01:30:00',
                                                     periods=4, freq='M')))

    def test_shifting_with_offsets(self):
        now = datetime(2018, 12, 2)
        self.assertEqual(datetime(2018, 12, 5, 0, 0), now + 3 * Day())
        self.assertEqual(now + 3 * Day(), now + relativedelta(days=3))
        self.assertEqual(datetime(2018, 12, 31, 0, 0), now + MonthEnd())
        self.assertEqual(datetime(2019, 1, 31, 0, 0), now + MonthEnd(2))

        self.assertEqual(MonthEnd().rollforward(now), now + MonthEnd())
        self.assertEqual(MonthEnd().rollback(now), now + MonthEnd(-1))


if __name__ == '__main__':
    unittest.main()
