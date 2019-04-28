#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestMathStatistical(unittest.TestCase):
    def test_aggregation(self):
        arr = np.array([[15, 7, -5, -3], [1, 2, -2, 9]])
        self.assertEqual(3, arr.mean())
        self.assertTrue((np.mean(arr) == arr.mean()).all())
        self.assertEqual(24, arr.sum())

    def test_axis(self):
        arr = np.array([[15, 7, -5, -3], [1, 2, -2, 9]])
        self.assertTrue((np.array([3.5, 2.5]) == arr.mean(axis=1)).all())
        self.assertTrue((np.array([8, 4.5, -3.5, 3]) == arr.mean(axis=0)).all())

    def test_cumulation(self):
        arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue((np.array([[0, 1, 2], [3, 5, 7], [9, 12, 15]]) == arr.cumsum(axis=0)).all())
        self.assertTrue((np.array([[0, 0, 0], [3, 12, 60], [6, 42, 336]]) == arr.cumprod(axis=1)).all())


if __name__ == '__main__':
    unittest.main()
