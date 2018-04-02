#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestTransposeArrSwapAxes(unittest.TestCase):
    def test_transpose(self):
        arr = np.arange(6).reshape(3, 2)
        self.assertTrue((np.arange(6).reshape((2, 3), order='F') == arr.T).all())

    def test_dot_product(self):
        arr = np.array([[1, 0, 2], [2, 0, 1]])
        self.assertTrue((np.array([[5, 4], [4, 5]]) == np.dot(arr, arr.T)).all())

    def test_transpose(self):
        arr = np.arange(12).reshape(2, 3, 2)
        self.assertTrue(
            (np.array([[[0, 2, 4], [1, 3, 5]], [[6, 8, 10], [7, 9, 11]]]) == arr.transpose((0, 2, 1))).all())
        self.assertTrue(
            (np.array([[[0, 1], [6, 7]], [[2, 3], [8, 9]], [[4, 5], [10, 11]]]) == arr.transpose((1, 0, 2))).all())
        self.assertTrue(
            (np.array([[[0, 6], [1, 7]], [[2, 8], [3, 9]], [[4, 10], [5, 11]]]) == arr.transpose((1, 2, 0))).all())
        self.assertTrue(
            (np.array([[[0, 2, 4], [6, 8, 10]], [[1, 3, 5], [7, 9, 11]]]) == arr.transpose((2, 0, 1))).all())
        self.assertTrue(
            (np.array([[[0, 6], [2, 8], [4, 10]], [[1, 7], [3, 9], [5, 11]]]) == arr.transpose((2, 1, 0))).all())

    def test_swap(self):
        arr = np.arange(12).reshape(2, 3, 2)
        self.assertTrue((arr.swapaxes(0, 1) == arr.swapaxes(1, 0)).all())
        self.assertTrue((arr.swapaxes(0, 2) == arr.swapaxes(2, 0)).all())
        self.assertTrue((arr.swapaxes(1, 2) == arr.swapaxes(2, 1)).all())

        self.assertTrue(
            (np.array([[[0, 1], [6, 7]], [[2, 3], [8, 9]], [[4, 5], [10, 11]]]) == arr.swapaxes(0, 1)).all())
        self.assertTrue((np.array([[[0, 6], [2, 8], [4, 10]], [[1, 7], [3, 9], [5, 11]]]) == arr.swapaxes(0, 2)).all())
        self.assertTrue((np.array([[[0, 2, 4], [1, 3, 5]], [[6, 8, 10], [7, 9, 11]]]) == arr.swapaxes(1, 2)).all())


if __name__ == '__main__':
    unittest.main()
