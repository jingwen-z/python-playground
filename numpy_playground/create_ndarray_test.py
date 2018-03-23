#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestCreationNdarray(unittest.TestCase):
    def test_ndarray_attr(self):
        data1 = [6, 7.5, 8, 0, 1]
        arr1 = np.array(data1)
        data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
        arr2 = np.array(data2)

        self.assertEqual(1, arr1.ndim)
        self.assertEqual(2, arr2.ndim)
        self.assertEqual((5,), arr1.shape)
        self.assertEqual((2, 4), arr2.shape)
        self.assertEqual('float64', arr1.dtype)
        self.assertEqual('int64', arr2.dtype)

    def test_zeros(self):
        zeros_1 = np.zeros(3)
        zeros_2 = np.zeros((4, 2))

        self.assertEqual(1, zeros_1.ndim)
        self.assertEqual(2, zeros_2.ndim)
        self.assertEqual((3,), zeros_1.shape)
        self.assertEqual((4, 2), zeros_2.shape)
        self.assertEqual('float64', zeros_1.dtype)
        self.assertEqual('float64', zeros_2.dtype)

    def test_empty(self):
        empty_1 = np.empty((2, 3, 2))
        self.assertEqual(3, empty_1.ndim)
        self.assertEqual((2, 3, 2), empty_1.shape)
        self.assertEqual('float64', empty_1.dtype)

    def test_arange(self):
        arng = np.arange(5)
        self.assertEqual((5,), arng.shape)
        self.assertTrue(isinstance(arng, np.ndarray))


if __name__ == '__main__':
    unittest.main()
