#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

NAMES = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will'])
DATA = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])


class TestBooleanIndexing(unittest.TestCase):
    def test_bool_selection(self):
        self.assertTrue((np.array([True, False, False, True, False]) == (NAMES == 'Bob')).all())
        self.assertTrue((np.array([[0, 1], [6, 7]]) == DATA[NAMES == 'Bob']).all())

    def test_index_col(self):
        self.assertTrue((np.array([0, 6]) == DATA[NAMES == 'Bob', 0]).all())
        self.assertTrue((np.array([[1], [7]]) == DATA[NAMES == 'Bob', 1:]).all())

    def test_neg_selection(self):
        self.assertTrue((np.array([False, True, True, False, True]) == (NAMES != 'Bob')).all())
        self.assertTrue((np.array([[2, 3], [4, 5], [8, 9]]) == DATA[~(NAMES == 'Bob')]).all())

    def test_invert_gnl_cdt(self):
        cond = NAMES == 'Bob'
        self.assertTrue((np.array([[2, 3], [4, 5], [8, 9]]) == DATA[~cond]).all())

    def test_multi_bool_cdt(self):
        mask = (NAMES == 'Bob') | (NAMES == 'Will')
        self.assertTrue((np.array([True, False, True, True, True]) == mask).all())
        self.assertTrue((np.array([[0, 1], [4, 5], [6, 7], [8, 9]]) == DATA[mask]).all())

    def test_set_val_wbool(self):
        scope = DATA.copy()
        scope[scope < 5] = 0
        self.assertTrue((np.array([[0, 0], [0, 0], [0, 5], [6, 7], [8, 9]]) == scope).all())

    def test_select_whole_rwcol(self):
        scope = DATA.copy()
        scope[NAMES != 'Bob'] = 77
        self.assertTrue((np.array([[0, 1], [77, 77], [77, 77], [6, 7], [77, 77]]) == scope).all())


if __name__ == '__main__':
    unittest.main()
