#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd
from numpy import nan as NA


class TestRemovingDuplicates(unittest.TestCase):
    def test_duplicated(self):
        df = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                           'k2': [1, 1, 2, 3, 3, 4, 4]})
        expected = pd.Series([False] * 6 + [True])
        self.assertTrue((expected == df.duplicated()).all())

    def test_drop_duplicated(self):
        df = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                           'k2': [1, 1, 2, 3, 3, 4, 4]})
        pd.testing.assert_frame_equal(pd.DataFrame({'k1': ['one', 'two'] * 3,
                                                    'k2': [1, 1, 2, 3, 3, 4]}),
                                      df.drop_duplicates())

    def test_drop_duplicated_first(self):
        df = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                           'k2': [1, 1, 2, 3, 3, 4, 4]})
        pd.testing.assert_frame_equal(pd.DataFrame({'k1': ['one', 'two'],
                                                    'k2': [1, 1]}),
                                      df.drop_duplicates(['k1']))

    def test_drop_duplicated_last(self):
        df = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                           'k2': [1, 1, 2, 3, 3, 4, 4]})
        pd.testing.assert_frame_equal(
            pd.DataFrame({'k1': ['two', 'one', 'one', 'two'],
                          'k2': [1, 2, 3, 4]}, index=[1, 2, 4, 6]),
            df.drop_duplicates(['k2'], keep='last'))


class TestTransformWithFctOrMap(unittest.TestCase):
    def test_series_mapping(self):
        df = pd.DataFrame(
            {'food': ['bacon', 'pastrami', 'nova_lox', 'honey_ham'],
             'ounces': [4, 3, 12, 7.5]})
        meat_to_animal = {
            'bacon': 'pig',
            'pastrami': 'cow',
            'nova_lox': 'salmon',
            'honey_ham': 'pig'
        }
        df['animal'] = df['food'].map(meat_to_animal)

        expected = pd.DataFrame(
            {'food': ['bacon', 'pastrami', 'nova_lox', 'honey_ham'],
             'ounces': [4, 3, 12, 7.5],
             'animal': ['pig', 'cow', 'salmon', 'pig']},
            columns=['food', 'ounces', 'animal'])

        pd.testing.assert_frame_equal(expected, df)


class TestReplaceValues(unittest.TestCase):
    def test_replace_single(self):
        df = pd.Series([1, 3, -999, -1000, 7])
        pd.testing.assert_series_equal(pd.Series([1, 3, NA, -1000, 7]),
                                       df.replace(-999, NA))

    def test_replace_multiple(self):
        df = pd.Series([1, 3, -999, -1000, 7])
        pd.testing.assert_series_equal(pd.Series([1, 3, NA, 0, 7]),
                                       df.replace([-999, -1000], [NA, 0]))
        pd.testing.assert_series_equal(df.replace({-999: NA, -1000: 0}),
                                       df.replace([-999, -1000], [NA, 0]))


class TestRenamingAxisIndexes(unittest.TestCase):
    def test_rename_index_mapping(self):
        df = pd.DataFrame(np.arange(12).reshape((3, 4)),
                          index=['Ohio', 'Colorado', 'New York'],
                          columns=['one', 'two', 'three', 'four'])
        transform = lambda x: x[:4].upper()
        df.index = df.index.map(transform)
        self.assertTrue((['OHIO', 'COLO', 'NEW '] == df.index).all())

    def test_rename_wo_modify_original(self):
        df = pd.DataFrame(np.arange(12).reshape((3, 4)),
                          index=['Ohio', 'Colorado', 'New York'],
                          columns=['one', 'two', 'three', 'four'])
        self.assertTrue((['ONE', 'TWO', 'THREE', 'FOUR'] == df.rename(
            index=str.title, columns=str.upper).columns).all())

    def test_rename_dict(self):
        df = pd.DataFrame(np.arange(12).reshape((3, 4)),
                          index=['Ohio', 'Colorado', 'New York'],
                          columns=['one', 'two', 'three', 'four'])
        df.rename(index={'Ohio': 'INDIANA'}, columns={'three': 'peekaboo'},
                  inplace=True)
        self.assertTrue((['INDIANA', 'Colorado', 'New York'] == df.index).all())
        self.assertTrue(
            (['one', 'two', 'peekaboo', 'four'] == df.columns).all())


class TestDiscretizationAndBinning(unittest.TestCase):
    def test_cut(self):
        ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
        bins = [18, 25, 35, 60, 100]
        cats = pd.cut(ages, bins)

        self.assertTrue((np.array(
            [0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1]) == cats.codes).all())


class TestDummyVariables(unittest.TestCase):
    def test_get_dummies(self):
        df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a'],
                           'data': range(5)})
        expected = pd.DataFrame({'a': [0, 0, 1, 0, 1],
                                 'b': [1, 1, 0, 0, 0],
                                 'c': [0, 0, 0, 1, 0]},
                                dtype='uint8')
        pd.testing.assert_frame_equal(expected, pd.get_dummies(df['key']))

    def test_dummies_prefix(self):
        df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a'],
                           'data': range(5)})
        dummies = pd.get_dummies(df['key'], prefix='key')
        df_with_dummy = df[['data']].join(dummies)

        expected = pd.DataFrame({'data': [0, 1, 2, 3, 4],
                                 'key_a': [0, 0, 1, 0, 1],
                                 'key_b': [1, 1, 0, 0, 0],
                                 'key_c': [0, 0, 0, 1, 0]}, dtype='uint8')
        expected['data'] = expected['data'].astype('int')
        pd.testing.assert_frame_equal(expected, df_with_dummy)


if __name__ == '__main__':
    unittest.main()
