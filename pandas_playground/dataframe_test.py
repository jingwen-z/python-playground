#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd
from pandas import Series


class TestDF(unittest.TestCase):
    def test_creation(self):
        data = {'state': ['Ohio', 'Ohio', 'Nevada'],
                'year': [2000, 2001, 2001],
                'pop': [1.5, 1.7, 3.6]}
        df = pd.DataFrame(data)
        self.assertTrue((['pop', 'state', 'year'] == df.columns).all())

    def test_col_name(self):
        data = {'state': ['Ohio', 'Ohio', 'Nevada'],
                'year': [2000, 2001, 2001],
                'pop': [1.5, 1.7, 3.6]}
        df = pd.DataFrame(data, columns=['year', 'state', 'pop'])
        self.assertTrue((['year', 'state', 'pop'] == df.columns).all())

    def test_wrg_col_name(self):
        data = {'state': ['Ohio', 'Ohio', 'Nevada'],
                'year': [2000, 2001, 2001],
                'pop': [1.5, 1.7, 3.6]}
        df = pd.DataFrame(data, columns=['year', 'state', 'debt'])
        self.assertTrue(([True, True, True] == df['debt'].isnull()).all())

    def test_assign_series(self):
        data = {'state': ['Ohio', 'Ohio', 'Nevada'],
                'year': [2000, 2001, 2001],
                'pop': [1.5, 1.7, 3.6]}
        df = pd.DataFrame(data, columns=['year', 'state', 'debt'],
                          index=['one', 'two', 'three'])
        val = Series([-1.2, -3.2, -1.5], index=['one', 'two', 'three'])
        df['debt'] = val
        self.assertEqual(-1.2, df.loc['one', 'debt'])

    def test_del_col(self):
        data = {'state': ['Ohio', 'Ohio', 'Nevada'],
                'year': [2000, 2001, 2001],
                'pop': [1.5, 1.7, 3.6]}
        df = pd.DataFrame(data, columns=['year', 'state', 'debt'])
        df['eastern'] = df['state'] == 'Ohio'
        self.assertTrue(
            (['year', 'state', 'debt', 'eastern'] == df.columns).all())

        del df['eastern']
        self.assertTrue((['year', 'state', 'debt'] == df.columns).all())

    def test_nested_dict(self):
        pop = {'Nevada': {2001: 2.4, 2002: 2.9},
               'Ohio': {2000: 1.2, 2001: 2.1, 2002: 3.5}}
        df = pd.DataFrame(pop)
        self.assertTrue((['Nevada', 'Ohio'] == df.columns).all())
        self.assertTrue(([2000, 2001, 2002] == df.index).all())

    def test_transpose_df(self):
        df = pd.DataFrame({'Nevada': {2001: 2.4, 2002: 2.9},
                           'Ohio': {2000: 1.2, 2001: 2.1, 2002: 3.5}})
        self.assertTrue((['Nevada', 'Ohio'] == df.T.index).all())
        self.assertTrue(([2000, 2001, 2002] == df.T.columns).all())

    def test_specified_index(self):
        pop = {'Nevada': {2001: 2.4, 2002: 2.9},
               'Ohio': {2000: 1.2, 2001: 2.1, 2002: 3.5}}
        df = pd.DataFrame(pop, index=[2001, 2002, 2003])
        self.assertTrue((df.loc[2003, :].isnull()).all())

    def test_series_dicts(self):
        df1 = pd.DataFrame({'Nevada': {2001: 2.4, 2002: 2.9},
                            'Ohio': {2000: 1.2, 2001: 2.1, 2002: 3.5}})
        pdata = {'Ohio': df1['Ohio'][:-1], 'Nevada': df1['Nevada'][:2]}
        df2 = pd.DataFrame(pdata)

        rdata = {'Nevada': [np.NaN, 2.4], 'Ohio': [1.2, 2.1]}
        result = pd.DataFrame(rdata, index=[2000, 2001])

        pd.testing.assert_frame_equal(df2, result)

    def test_series_values(self):
        data = {'Nevada': [5, 2.4], 'Ohio': [1.2, 2.1]}
        df = pd.DataFrame(data, index=[2000, 2001])
        val = df.values
        arr = np.array([[5, 1.2], [2.4, 2.1]])
        self.assertTrue((val == arr).all())


if __name__ == '__main__':
    unittest.main()
