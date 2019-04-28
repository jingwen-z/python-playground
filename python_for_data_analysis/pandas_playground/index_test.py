# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd
import numpy as np


class TestIndexObj(unittest.TestCase):
    def test_create_index(self):
        labels = pd.Index(np.arange(3))
        obj = pd.Series([1.5, -2.5, 0], index=labels)
        self.assertTrue(([0, 1, 2] == obj.index).all())
        self.assertTrue(obj.index is labels)

    def test_fixed_size_Set(self):
        pop = {'Nevada': {2001: 2.4, 2002: 2.9},
               'Ohio': {2000: 1.2, 2001: 2.1, 2002: 3.5}}
        df = pd.DataFrame(pop)
        df.index.name = 'year'
        df.columns.name = 'state'

        self.assertTrue('Ohio' in df.columns)
        self.assertFalse(2003 in df.index)

    def test_append_ind(self):
        labels = pd.Index(np.arange(3))
        labels = labels.append(pd.Index([3]))
        obj = pd.Series([1.5, -2.5, 0, 1], index=labels)
        self.assertTrue((np.arange(4) == obj.index).all())

    def test_diff_ind(self):
        ind1 = pd.Index([1, 2, 3, 4])
        ind2 = pd.Index([3, 4, 5, 6])
        self.assertTrue(([1, 2] == ind1.difference(ind2)).all())
        self.assertTrue(([5, 6] == ind2.difference(ind1)).all())

    def test_intersection_ind(self):
        ind1 = pd.Index([1, 2, 3, 4])
        ind2 = pd.Index([3, 4, 5, 6])
        self.assertTrue(([3, 4] == ind1.intersection(ind2)).all())
        self.assertTrue(([3, 4] == ind2.intersection(ind1)).all())

    def test_union_ind(self):
        ind1 = pd.Index([1, 2, 3, 4])
        ind2 = pd.Index([3, 4, 5, 6])
        self.assertTrue(([1, 2, 3, 4, 5, 6] == ind1.union(ind2)).all())
        self.assertTrue(([1, 2, 3, 4, 5, 6] == ind2.union(ind1)).all())

    def test_isin_ind(self):
        ind = pd.Index([1, 2, 3])
        self.assertTrue(([False, True, False] == ind.isin([2])).all())

    def test_delete_ind(self):
        ind = pd.Index([1, 2, 3])
        self.assertTrue(([1, 3] == ind.delete(loc=1)).all())

    def test_drop_ind(self):
        ind = pd.Index([1, 2, 3])
        self.assertTrue(([2, 3] == ind.drop(labels=1)).all())

    def test_insert_ind(self):
        ind = pd.Index([1, 2, 3])
        self.assertTrue(([0, 1, 2, 3] == ind.insert(loc=0, item=0)).all())

    def test_ismonotonic_ind(self):
        ind1 = pd.Index([1, 2, 3])
        ind2 = pd.Index([3, 2, 3])
        self.assertTrue(ind1.is_monotonic)
        self.assertFalse(ind2.is_monotonic)

    def test_isunique_ind(self):
        ind1 = pd.Index([1, 2, 3])
        ind2 = pd.Index([2, 2, 3])
        self.assertTrue(ind1.is_unique)
        self.assertFalse(ind2.is_unique)

    def test_unique_ind(self):
        ind = pd.Index([2, 2, 3])
        self.assertTrue(([2, 3] == ind.unique()).all())


if __name__ == '__main__':
    unittest.main()
