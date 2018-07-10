#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import unittest
import pandas as pd


class TestReIdentifiers(unittest.TestCase):
    def test_any_number(self):
        value = '''
        One is 1, ten is 10, one hundred is 100.
        '''
        p = r'\d{1,3}'
        self.assertEqual(['1', '10', '100'], re.findall(p, value))

    def test_any_character(self):
        value = '''
        One is 1, ten is 10, one hundred is 100.
        '''
        p = r'\w+'
        # p = r'[a-zA-Z]+'
        self.assertEqual(['One', 'is', '1', 'ten', 'is', '10',
                          'one', 'hundred', 'is', '100'],
                         re.findall(p, value))

    def test_space(self):
        value = 'One is 1.'
        p = r'\s'
        self.assertEqual([' ', ' '], re.findall(p, value))


class TestReModifiers(unittest.TestCase):
    def test_match_0_or_more(self):
        value = 'One = 1.'
        p = r'\d*'
        self.assertEqual(['', '', '', '', '', '', '1', '', ''],
                         re.findall(p, value))

    def test_match_1_or_more(self):
        value = 'One = 1.'
        p = r'\d+'
        self.assertEqual(['1'], re.findall(p, value))

    def test_match_0_or_1(self):
        value = 'One = 1.'
        p = r'\W?'
        self.assertEqual(['', '', '', ' ', '=', ' ', '', '.', ''],
                         re.findall(p, value))

    def test_match_starting_and_ending(self):
        p = r'^[^1]{2}[^3]$'
        self.assertEqual([], re.findall(p, '1=2'))
        self.assertEqual([], re.findall(p, '1=1'))
        self.assertEqual([], re.findall(p, '2=3'))
        self.assertEqual([], re.findall(p, '111'))
        self.assertEqual([], re.findall(p, '121'))
        self.assertEqual([], re.findall(p, '212'))
        self.assertEqual(['2=1'], re.findall(p, '2=1'))
        self.assertEqual(['2=2'], re.findall(p, '2=2'))
        self.assertEqual(['221'], re.findall(p, '221'))

    def test_character_class(self):
        p = r'^[A-Z]+[a-z]+'
        self.assertEqual(['Apple'], re.findall(p, 'Apple'))
        self.assertEqual(['APple'], re.findall(p, 'APple'))
        self.assertEqual([], re.findall(p, 'APPLE'))
        self.assertEqual([], re.findall(p, 'apple'))
        self.assertEqual([], re.findall(p, 'appLE'))

    def test_group(self):
        p = r'([a-z0-9]+)@([a-z]*)\.([a-z]{2,4})'
        self.assertEqual([('dfsdfa567', 'gmail', 'comm')],
                         re.findall(p, 'dfsdfa567@gmail.comm'))
        self.assertEqual([('dfa567', 'gmail', 'fr')],
                         re.findall(p, 'DFSdfa567@gmail.fr'))
        self.assertEqual([('567dfsdfa', 'gmail', 'com')],
                         re.findall(p, '567dfsdfa@gmail.com'))

    def test_findall_in_df(self):
        df = pd.DataFrame({'Name': ['Amy', 'Ben', 'Christine', 'David'],
                           'Birthday': ['1980-02-12', '2013-02-14',
                                        '1983-11-23', '1969-05-30'],
                           'Email': ['amy.l@hotmail.com', 'benmartni@gmail.fr',
                                     'c.mousse@example.com', 'd_zhang@fp.fr']},
                          columns=['Name', 'Birthday', 'Email'])
        p = r'^[a-z]+@[a-z]+\.[a-z]{2,3}'

        expected = pd.Series([[], ['benmartni@gmail.fr'], [], []])
        expected.name = 'Email'

        pd.testing.assert_series_equal(expected,
                                       df['Email'].apply(
                                           lambda x: re.findall(p, x)))

    def test_replace_in_df(self):
        df = pd.DataFrame({'Name': ['Amy', 'Ben', 'Christine', 'David'],
                           'Birthday': ['1980-02-12', '2013-02-14',
                                        '1983-11-23', '1969-05-30'],
                           'Email': ['amy.l@hotmail.com', 'benmartni@gmail.fr',
                                     'c.mousse@example.com', 'd_zhang@fp.fr']},
                          columns=['Name', 'Birthday', 'Email'])
        p = r'[@]'
        df['Email'] = df['Email'].apply(lambda x: re.sub(p, '[at]', x))

        expected = pd.DataFrame({'Name': ['Amy', 'Ben', 'Christine', 'David'],
                                 'Birthday': ['1980-02-12', '2013-02-14',
                                              '1983-11-23', '1969-05-30'],
                                 'Email': ['amy.l[at]hotmail.com',
                                           'benmartni[at]gmail.fr',
                                           'c.mousse[at]example.com',
                                           'd_zhang[at]fp.fr']},
                                columns=['Name', 'Birthday', 'Email'])

        pd.testing.assert_frame_equal(df, expected)


if __name__ == '__main__':
    unittest.main()
