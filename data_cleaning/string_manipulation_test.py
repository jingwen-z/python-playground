#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import re
import numpy as np
import pandas as pd

VAL = 'a,b, guido'
PIECES = [x.strip() for x in VAL.split(',')]
FIRST, SECOND, THIRD = PIECES

MAIL_ADR = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

DATA = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}


class TestStringObjMethods(unittest.TestCase):
    def test_join(self):
        self.assertEqual('a::b::guido', '::'.join(PIECES))

    def test_detect_a_substr(self):
        self.assertTrue('guido' in VAL)
        self.assertEqual(1, VAL.index(','))
        self.assertTrue(VAL.index(','), VAL.find(','))

    def test_count(self):
        self.assertEqual(2, VAL.count(','))

    def test_replace(self):
        self.assertEqual('a::b:: guido', VAL.replace(',', '::'))

    def test_upper(self):
        self.assertEqual('B', VAL[2].upper())


class TestRegularExpressions(unittest.TestCase):
    def test_whitespace_char(self):
        text = 'foo     bar\t baz   \tqux'
        self.assertEqual(['foo', 'bar', 'baz', 'qux'], re.split('\s+', text))

        regex = re.compile('\s+')
        self.assertEqual(['     ', '\t ', '   \t'], regex.findall(text))

    def test_findall(self):
        pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
        regex = re.compile(pattern, flags=re.IGNORECASE)

        expected = ['dave@google.com', 'steve@gmail.com',
                    'rob@gmail.com', 'ryan@yahoo.com']
        self.assertEqual(expected, regex.findall(MAIL_ADR))

    def test_search(self):
        pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
        regex = re.compile(pattern, flags=re.IGNORECASE)

        m = regex.search(MAIL_ADR)
        self.assertEqual('dave@google.com', MAIL_ADR[m.start():m.end()])

    def test_match(self):
        pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
        regex = re.compile(pattern, flags=re.IGNORECASE)

        self.assertEqual(None, regex.match(MAIL_ADR))

    def test_find_sinultaneously(self):
        pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
        regex = re.compile(pattern, flags=re.IGNORECASE)

        m = regex.match('wesm@bright.net')
        self.assertEqual(('wesm', 'bright', 'net'), m.groups())
        self.assertEqual(('Username: wesm, Domain: bright, Suffix: net'),
                         regex.sub(r'Username: \1, Domain: \2, Suffix: \3',
                                   'wesm@bright.net'))


class TestVectorizedStringFunctions(unittest.TestCase):
    def test_str_contains(self):
        ser = pd.Series(DATA)
        expected = pd.Series({'Dave': False, 'Steve': True,
                              'Rob': True, 'Wes': np.nan})
        pd.testing.assert_series_equal(expected, ser.str.contains('gmail'))

    def test_str_findall(self):
        ser = pd.Series(DATA)
        pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

        expected = pd.Series({'Dave': [('dave', 'google', 'com')],
                              'Rob': [('rob', 'gmail', 'com')],
                              'Steve': [('steve', 'gmail', 'com')],
                              'Wes': np.nan})

        pd.testing.assert_series_equal(expected,
                                       ser.str.findall(pattern,
                                                       flags=re.IGNORECASE))

    def test_str_match(self):
        ser = pd.Series(DATA)
        pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

        expected = pd.Series({'Dave': True, 'Rob': True,
                              'Steve': True, 'Wes': np.nan})
        pd.testing.assert_series_equal(expected,
                                       ser.str.match(pattern,
                                                     flags=re.IGNORECASE))

    def test_str(self):
        ser = pd.Series(DATA)
        expected = pd.Series({'Dave': 'dave@', 'Rob': 'rob@g',
                              'Steve': 'steve', 'Wes': np.nan})
        pd.testing.assert_series_equal(expected, ser.str[:5])


if __name__ == '__main__':
    unittest.main()
