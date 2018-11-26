#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from datetime import timedelta

from dateutil.parser import parse

STAMP = datetime(2011, 1, 3)
STR_VALUE = '2011-01-03'


class TestDateTime(unittest.TestCase):
    def test_basic(self):
        delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
        self.assertEqual(delta, timedelta(926, 56700))
        self.assertEqual(delta.days, 926)
        self.assertEqual(delta.seconds, 56700)

    def test_timedelta(self):
        start = datetime(2011, 1, 7)
        self.assertEqual(start + timedelta(12),
                         datetime(2011, 1, 19, 0, 0))
        self.assertEqual(start - 2 * timedelta(12),
                         datetime(2010, 12, 14, 0, 0))


class TestDatetimeToString(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(STAMP), '2011-01-03 00:00:00')

    def test_strftime(self):
        self.assertEqual(STAMP.strftime('%Y-%m-%d'), '2011-01-03')


class TestStringToDatetime(unittest.TestCase):
    def test_strptime(self):
        self.assertEqual(datetime.strptime(STR_VALUE, '%Y-%m-%d'),
                         datetime(2011, 1, 3, 0, 0))

    def test_parse_auto(self):
        self.assertEqual(parse(STR_VALUE), datetime(2011, 1, 3, 0, 0))

    def test_parse_human(self):
        self.assertEqual(parse('Jan 31, 1997 10:45 PM'),
                         datetime(1997, 1, 31, 22, 45))

    def test_parse_dayfirst(self):
        self.assertEqual(parse('6/12/2011', dayfirst=True),
                         datetime(2011, 12, 6, 0, 0))


if __name__ == '__main__':
    unittest.main()
