#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

ARR_1 = np.empty((8, 2))

for i in range(8):
    ARR_1[i] = i

ARR_2 = np.arange(16).reshape((8, 2))
print(ARR_2)


class TestFancyIndexing(unittest.TestCase):
    def test_row_subset(self):
        self.assertTrue((np.array([[3, 3], [7, 7], [5, 5], [1, 1]]) == ARR_1[[3, 7, 5, 1]]).all())
        self.assertTrue((np.array([[5, 5], [6, 6], [2, 2]]) == ARR_1[[-3, -2, -6]]).all())

    def test_multi_idx_arr(self):
        self.assertTrue((np.array([11, 15, 13, 5]) == ARR_2[[5, 7, 6, 2], [1]]).all())
        self.assertTrue((np.array([[11, 10], [15, 14], [13, 12]]) == ARR_2[[5, 7, 6]][:, [1, 0]]).all())


if __name__ == '__main__':
    unittest.main()
