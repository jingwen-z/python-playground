# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

DF = pd.DataFrame({'key': ['a', 'b', 'c'] * 4, 'value': np.arange(12)})

TIMES = pd.date_range('2017-05-20 00:00', freq='1min', periods=15)
TIMES_DF = pd.DataFrame({'time': TIMES, 'value': np.arange(15)})


class TestGroupTransforms(unittest.TestCase):
    def test_transform(self):
        g = DF.groupby('key').value
        self.assertEqual(g.mean()['a'], 4.5)

        result = g.transform(lambda x: x.mean())
        self.assertTrue(
            result.loc[0,] == result.loc[3,] == result.loc[6,] == 4.5)

        self.assertTrue(
            (g.transform(lambda x: x * 2) == g.apply(lambda x: x * 2)).all())


class TestTimeResampling(unittest.TestCase):
    def test_resample(self):
        resample_by_freq = TIMES_DF.set_index('time').resample('5min').count()
        self.assertTrue(
            (resample_by_freq.index == pd.DatetimeIndex(['2017-05-20 00:00:00',
                                                         '2017-05-20 00:05:00',
                                                         '2017-05-20 00:10:00'])).all())


if __name__ == '__main__':
    unittest.main()
