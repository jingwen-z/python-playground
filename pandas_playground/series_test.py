#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd
from pandas import Series


class TestSeries(unittest.TestCase):
    def test_default_index(self):
        obj = pd.Series([4, -7, 2, 1])
        self.assertTrue((np.array([4, -7, 2, 1]) == obj.values).all())
        self.assertTrue(
            (pd.RangeIndex(start=0, stop=4, step=1) == obj.index).all())

    def test_identify_index(self):
        obj2 = pd.Series([4, -7, 2], index=['c', 'b', 'a'])
        self.assertTrue(
            (pd.Index(['c', 'b', 'a'], dtype='object') == obj2.index).all())
        self.assertEqual(-7, obj2['b'])

    def test_update_value(self):
        obj2 = pd.Series([4, -7, 2], index=['c', 'b', 'a'])
        obj2['c'] = 1
        self.assertTrue(
            (obj2[['a', 'c']] == pd.Series([2, 1], index=['a', 'c'])).all())

    def test_operations(self):
        obj = pd.Series([4, -7, 2], index=['c', 'b', 'a'])
        self.assertTrue(
            (Series([4, 2], index=['c', 'a']) == obj[obj > 0]).all())
        self.assertTrue(
            (Series([8, -14, 4], index=['c', 'b', 'a']) == obj * 2).all())

    def test_in(self):
        obj = pd.Series([4, -7, 2], index=['c', 'b', 'a'])
        self.assertTrue('b' in obj)
        self.assertFalse('d' in obj)

    def test_dict_series(self):
        sdata = {'Ohio': 35000, 'Texas': 80000, 'Utah': 9000}
        obj = pd.Series(sdata)
        self.assertTrue((Series([35000, 80000, 9000],
                                index=['Ohio', 'Texas', 'Utah']) == obj).all())

    def test_dict_index(self):
        sdata = {'Ohio': 35000, 'Texas': 80000, 'Utah': 9000}
        states = ['California', 'Ohio', 'Texas']
        obj = pd.Series(sdata, index=states)
        bool_obj = Series([True, False, False],
                          index=['California', 'Ohio', 'Texas'])
        self.assertTrue((bool_obj == pd.isnull(obj)).all())
        self.assertTrue((bool_obj == obj.isnull()).all())

    def test_arithmetic_ope(self):
        obj1 = pd.Series({'Ohio': 35000, 'Texas': 80000, 'Utah': 9000})
        obj2 = pd.Series({'Ohio': 25000, 'Texas': 8000, 'Utah': 5000})
        total = pd.Series({'Ohio': 60000, 'Texas': 88000, 'Utah': 14000})

        self.assertTrue((obj1 + obj2 == total).all())

    def test_name(self):
        obj = pd.Series({'Ohio': 35000, 'Texas': 80000, 'Utah': 9000})
        obj.name = 'population'
        obj.index.name = 'state'
        self.assertEqual('population', obj.name)
        self.assertEqual('state', obj.index.name)

    def test_alter_index(self):
        obj = Series([4, -7, 2, 1])
        obj.index = ['A', 'B', 'C', 'D']
        result = Series([4, -7, 2, 1], index=['A', 'B', 'C', 'D'])
        self.assertTrue((result == obj).all())


if __name__ == '__main__':
    unittest.main()
