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

    def test_array_append(self):
        arr = np.array([3, 5, 1, 3])
        arr = np.append(arr, [7])
        self.assertTrue((np.array([3, 5, 1, 3, 7]) == arr).all())

    def test_array_insert(self):
        arr = np.array([[1, 1], [2, 2], [3, 3]])
        arr = np.insert(arr, 1, 5, axis=1)
        self.assertTrue((np.array([[1, 5, 1], [2, 5, 2], [3, 5, 3]]) == arr).all())

    def test_array_delete(self):
        arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        arr_1 = np.delete(arr, 1, 0)
        arr_2 = np.delete(arr, [1, 3, 5], None)
        self.assertTrue((np.array([[1, 2, 3, 4], [9, 10, 11, 12]]) == arr_1).all())
        self.assertTrue((np.array([1, 3, 5, 7, 8, 9, 10, 11, 12]) == arr_2).all())

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

    def test_full(self):
        full_1 = np.full(shape=(2, 3), fill_value=7)
        self.assertEqual(2, full_1.ndim)
        self.assertEqual((2, 3), full_1.shape)
        self.assertTrue(isinstance(full_1, np.ndarray))

    def test_arange(self):
        arng = np.arange(5)
        self.assertEqual((5,), arng.shape)
        self.assertTrue(isinstance(arng, np.ndarray))


if __name__ == '__main__':
    unittest.main()
