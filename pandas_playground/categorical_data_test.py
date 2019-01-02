# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

FRUITS = ['apple', 'orange', 'apple', 'apple'] * 2

DF = pd.DataFrame({'fruit': FRUITS, 'basket_id': np.arange(len(FRUITS)),
                   'count': np.arange(2, 10),
                   'weight': np.arange(0.2, 1, 0.1)},
                  columns=['fruit', 'basket_id', 'count', 'weight'])


class TestBasic(unittest.TestCase):
    def test_value_counts(self):
        values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
        val_counts = pd.value_counts(values)
        pd.testing.assert_series_equal(val_counts,
                                       pd.Series([6, 2],
                                                 index=['apple', 'orange']))

    def test_take(self):
        values = pd.Series([0, 1, 0, 0] * 2)
        dim = pd.Series(['apple', 'orange'])
        pd.testing.assert_series_equal(dim.take(values),
                                       pd.Series(['apple', 'orange',
                                                  'apple', 'apple'] * 2,
                                                 index=[0, 1, 0, 0] * 2))


class TestCategoricalTypeInPandas(unittest.TestCase):
    def test_astype(self):
        fruit_cat = DF['fruit'].astype('category')
        self.assertEqual('category', fruit_cat.dtype)

    def test_categories_codes(self):
        fruit_cat = DF['fruit'].astype('category')
        c = fruit_cat.values
        self.assertTrue((np.array([0, 1, 0, 0, 0, 1, 0, 0]) == c.codes).all())
        self.assertTrue((pd.Index(['apple', 'orange']) == c.categories).all())

    def test_categorical(self):
        categories = ['foo', 'bar', 'baz']
        codes = [0, 1, 2, 0, 0, 1]
        self.assertTrue(
            (pd.Categorical.from_codes(codes, categories) == pd.Categorical(
                ['foo', 'bar', 'baz', 'foo', 'foo', 'bar'])).all())


if __name__ == '__main__':
    unittest.main()
