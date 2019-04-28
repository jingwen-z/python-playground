#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

ARR_2D = np.array([[1, 2], [3, 4], [5, 6]])
ARR_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


class TestIndexingSlicing(unittest.TestCase):
    def test_1d_indexing(self):
        arr = np.arange(6)
        self.assertTrue((np.array([0, 1, 2, 3, 4, 5]) == arr).all())
        self.assertEqual(2, arr[2])
        self.assertTrue((np.array([2, 3, 4]) == arr[2:5]).all())

    def test_1d_assign_value(self):
        arr = np.arange(6)
        arr[3:5] = 7
        self.assertTrue((np.array([0, 1, 2, 7, 7, 5]) == arr).all())

    def test_bare_slicing(self):
        arr = np.arange(6)
        arr_slice = arr[3:5]
        arr_slice[:] = 10
        self.assertTrue((np.array([0, 1, 2, 10, 10, 5]) == arr).all())

        arr_slice[:] = [3, 4]
        self.assertTrue((np.array([0, 1, 2, 3, 4, 5]) == arr).all())

    def test_copy_array(self):
        arr = np.arange(6)
        arr_copy = arr[3:5].copy()
        self.assertTrue((np.array([3, 4]) == arr_copy).all())
        self.assertTrue((np.array([0, 1, 2, 3, 4, 5]) == arr).all())

    def test_2d_indexing(self):
        self.assertTrue((np.array([5, 6]) == ARR_2D[2]).all())

    def test_2d_idx_slicing(self):
        self.assertTrue((np.array([[1, 2], [3, 4]]) == ARR_2D[:2]).all())
        self.assertTrue((np.array([[3], [5]]) == ARR_2D[1:, :1]).all())
        self.assertTrue((np.array([[3]]) == ARR_2D[1, :1]).all())
        self.assertTrue((np.array([[1], [3], [5]]) == ARR_2D[:, :1]).all())

    def test_2d_assign_value(self):
        arr_2 = ARR_2D.copy()
        arr_2[1, 1:] = 0
        self.assertTrue((np.array([[1, 2], [3, 0], [5, 6]]) == arr_2).all())

    def test_access_recursively(self):
        self.assertEqual(2, ARR_2D[0][1])
        self.assertEqual(2, ARR_2D[0, 1])
        self.assertTrue(ARR_2D[0][1] == ARR_2D[0, 1])

    def test_3d_indexing(self):
        self.assertEqual(3, ARR_3D.ndim)
        self.assertEqual((2, 2, 3), ARR_3D.shape)
        self.assertTrue((np.array([[7, 8, 9], [10, 11, 12]]) == ARR_3D[1]).all())
        self.assertTrue((np.array([7, 8, 9]) == ARR_3D[1, 0]).all())

    def test_3d_2steps_indexing(self):
        x = ARR_3D[1]
        self.assertTrue((np.array([7, 8, 9]) == x[0]).all())

    def test_3d_assign_value(self):
        arr_3 = ARR_3D.copy()
        old_values = arr_3[0].copy()
        arr_3[0] = 77
        self.assertTrue((np.array([[77, 77, 77], [77, 77, 77]]) == arr_3[0]).all())

        arr_3[0] = old_values
        self.assertTrue((np.array([[1, 2, 3], [4, 5, 6]]) == arr_3[0]).all())


if __name__ == '__main__':
    unittest.main()
