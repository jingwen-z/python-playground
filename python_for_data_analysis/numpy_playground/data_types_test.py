#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestDataTypes(unittest.TestCase):
    def test_dtype(self):
        arr1 = np.array([1, 2, 3], dtype=np.float64)
        arr2 = np.array([1, 2, 3], dtype=np.int32)
        self.assertEqual('float64', arr1.dtype)
        self.assertEqual('int32', arr2.dtype)
        self.assertEqual(2.0, arr1[1])

    def test_type_convert_int2float(self):
        int_array = np.array([1, 2, 3, 4, 5])
        self.assertEqual('int64', int_array.dtype)
        float_array = int_array.astype(np.float64)
        self.assertEqual('float64', float_array.dtype)

    def test_type_convert_float2int(self):
        float_array = np.array([2.3, 4.6])
        int_array = float_array.astype(int)
        self.assertTrue((np.array([2, 4]) == int_array).all())

    def test_type_convert_str2float(self):
        str_array = np.array(['1.2', '5.7'], dtype=np.string_)
        float_array = str_array.astype(np.float64)
        self.assertTrue((np.array([1.2, 5.7]) == float_array).all())

    def test_type_convert_int2other(self):
        int_array = np.arange(3)
        other_float_array = np.array([.3, .7, .1, .9, .2], dtype=np.float64)
        float_array = int_array.astype(other_float_array.dtype)
        self.assertTrue((np.array([0., 1., 2.]) == float_array).all())


if __name__ == '__main__':
    unittest.main()
