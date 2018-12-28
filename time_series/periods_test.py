# -*- coding: utf-8 -*-

import unittest

import pandas as pd

P = pd.Period(2007, freq='A-DEC')


class TestPeriodBasic(unittest.TestCase):
    def test_operation_on_periods(self):
        self.assertTrue(P + 5 == pd.Period(2012, freq='A-DEC'))
        self.assertTrue(P - 2 == pd.Period(2005, freq='A-DEC'))


class TestPeriodFreqConversion(unittest.TestCase):
    def test_asfreq(self):
        self.assertTrue(
            P.asfreq('M', how='start') == pd.Period('2007-01', freq='M'))
        self.assertTrue(
            P.asfreq('M', how='end') == pd.Period('2007-12', freq='M'))


if __name__ == '__main__':
    unittest.main()
