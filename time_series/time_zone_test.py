# -*- coding: utf-8 -*-

import math
import unittest
from datetime import datetime

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd

TS = pd.Series(np.arange(5),
               index=pd.date_range('3/9/2012 9:30', periods=5, freq='D'))


class TestTZLocalizationandConversion(unittest.TestCase):
    def test_daterange_tz(self):
        result = pd.date_range('3/9/2012 9:30', periods=5, freq='D', tz='UTC')
        self.assertTrue((result ==
                         pd.DatetimeIndex(['2012-03-09 09:30:00+00:00',
                                           '2012-03-10 09:30:00+00:00',
                                           '2012-03-11 09:30:00+00:00',
                                           '2012-03-12 09:30:00+00:00',
                                           '2012-03-13 09:30:00+00:00'])).all())

    def test_tz_localize(self):
        ts_utc = TS.tz_localize('UTC')
        self.assertTrue((ts_utc.index ==
                         pd.DatetimeIndex(['2012-03-09 09:30:00+00:00',
                                           '2012-03-10 09:30:00+00:00',
                                           '2012-03-11 09:30:00+00:00',
                                           '2012-03-12 09:30:00+00:00',
                                           '2012-03-13 09:30:00+00:00'])).all())

    def test_tz_convert(self):
        ts_utc = TS.tz_localize('UTC')
        ts_nyc = ts_utc.tz_convert('America/New_York')
        self.assertTrue((ts_nyc.index == pd.DatetimeIndex(
            ['2012-03-09 04:30:00-05:00', '2012-03-10 04:30:00-05:00',
             '2012-03-11 05:30:00-04:00', '2012-03-12 05:30:00-04:00',
             '2012-03-13 05:30:00-04:00'])).all())

    def test_method_datetimeindex(self):
        ts_loc_idx = TS.index.tz_localize('Asia/Shanghai')
        self.assertTrue(
            (ts_loc_idx == TS.tz_localize('Asia/Shanghai').index).all())


class TestOperationsWithTZ(unittest.TestCase):
    def test_tz_aware(self):
        stamp_utc = pd.Timestamp('2011-03-12 04:00').tz_localize('utc')
        self.assertEqual(stamp_utc.value,
                         stamp_utc.tz_convert('America/New_York').value)

    def test_offset(self):
        stamp = pd.Timestamp('2018-03-25 01:30', tz='Europe/Paris')
        self.assertTrue(
            (stamp == pd.DatetimeIndex(['2018-03-25 01:30:00+01:00'])).all())
        self.assertTrue((stamp + Hour() == pd.DatetimeIndex(
            ['2018-03-25 03:30:00+02:00'])).all())


if __name__ == '__main__':
    unittest.main()
