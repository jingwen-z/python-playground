#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestCdtLogic(unittest.TestCase):
    def test_where_simple(self):
        x = np.array([1.2, 3, 5, 6.1])
        y = np.array([2, 1.5, 2.4, 7])
        cdt = np.array([True, True, False, False])
        result = np.where(cdt, x, y)
        self.assertTrue((np.array([1.2, 3, 2.4, 7]) == result).all())

    def test_where_matrix(self):
        arr = np.array([[5, 7, -6, -3], [1, 2, -4, 5]])
        result_1 = np.where(arr > 0, 2, -2)
        result_2 = np.where(arr > 0, 2, arr)
        self.assertTrue((np.array([[2, 2, -2, -2], [2, 2, -2, 2]]) == result_1).all())
        self.assertTrue((np.array([[2, 2, -6, -3], [2, 2, -4, 2]]) == result_2).all())


if __name__ == '__main__':
    unittest.main()
