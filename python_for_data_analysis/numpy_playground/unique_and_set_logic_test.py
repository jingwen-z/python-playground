#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestSetLogic(unittest.TestCase):
    def test_unique(self):
        arr_1 = np.array(['a', 'c', 'b', 'a'])
        arr_2 = np.array([3, 5, 4, 3])
        self.assertTrue((np.array(['a', 'b', 'c']) == np.unique(arr_1)).all())
        self.assertTrue((np.array([3, 4, 5]) == np.unique(arr_2)).all())

    def test_unique_alter(self):
        arr = np.array(['a', 'c', 'b', 'a'])
        self.assertTrue((sorted(set(arr)) == np.unique(arr)).all())

    def test_in1d(self):
        values = np.array([5, 3, 2, 6, 7])
        # compute a bool array indicating whether each element of values is contained in [7, 2, 3]
        self.assertTrue((np.array([False, True, True, False, True]) == np.in1d(values, [7, 2, 3])).all())

    def test_intersect1d(self):
        arr_1 = np.array([3, 7, 5])
        arr_2 = np.array([5, 7, 1, 2])
        # compute the sorted common elements in arr_1 and arr_2
        self.assertTrue((np.array([False, True, True]) == np.in1d(arr_1, arr_2)).all())

    def test_setdiff1d(self):
        arr_1 = np.array([3, 7, 6])
        arr_2 = np.array([5, 7, 1, 2])
        self.assertTrue((np.array([3, 6]) == np.setdiff1d(arr_1, arr_2)).all())
        self.assertTrue((np.array([1, 2, 5]) == np.setdiff1d(arr_2, arr_1)).all())

    def test_setxor1d(self):
        arr_1 = np.array([3, 7, 1])
        arr_2 = np.array([5, 7, 1, 2])
        self.assertTrue((np.array([2, 3, 5]) == np.setxor1d(arr_1, arr_2)).all())


if __name__ == '__main__':
    unittest.main()
