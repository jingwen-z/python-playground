#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestUniversalFunctions(unittest.TestCase):
    def test_simple_element(self):
        arr = np.array([0, 1, 4])
        self.assertTrue((np.array([0, 1, 2]) == np.sqrt(arr)).all())

    def test_binary_ufuncs(self):
        x = np.array([4, 3, 2, 6])
        y = np.array([7, 3, 6, 2])
        self.assertTrue((np.array([7, 3, 6, 6]) == np.maximum(x, y)).all())

    def test_multi_results(self):
        arr = np.array([2, 3.6, -5])
        reminders, integers = np.modf(arr)
        self.assertTrue(-0. == reminders[2])
        self.assertTrue((np.array([2, 3, -5]) == integers).all())

    def test_out_opt(self):
        arr = np.array([0, 1, 0.04])
        np.sqrt(arr, arr)
        self.assertTrue((np.array([0, 1, 0.2]) == arr).all())

    def test_abs(self):
        arr = np.array([2, 3.6, -5, -2.7])
        self.assertTrue((np.array([2, 3.6, 5, 2.7]) == np.abs(arr)).all())
        self.assertTrue((np.array([2, 3.6, 5, 2.7]) == np.fabs(arr)).all())

    def test_square(self):
        arr = np.array([0, 1, 2])
        self.assertTrue((np.array([0, 1, 4]) == np.square(arr)).all())

    def test_sign(self):
        arr = np.array([-2, 0, 2])
        self.assertTrue((np.array([-1, 0, 1]) == np.sign(arr)).all())

    def test_ceil(self):
        arr = np.array([-2.2, 0, 2.2])
        self.assertTrue((np.array([-2, 0, 3]) == np.ceil(arr)).all())

    def test_floor(self):
        arr = np.array([-2.2, 0, 2.2])
        self.assertTrue((np.array([-3, 0, 2]) == np.floor(arr)).all)


if __name__ == '__main__':
    unittest.main()
