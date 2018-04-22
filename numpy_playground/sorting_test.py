#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestSorting(unittest.TestCase):
    def test_sorting_1d(self):
        arr = np.array([3, 5, 1, -9, 7])
        arr.sort()
        self.assertTrue((np.array([-9, 1, 3, 5, 7]) == arr).all())

    def test_sorting_nd(self):
        arr = np.array([[-5, 2, 0, 23], [-4, -9, 3, 2]])
        arr.sort(1)
        self.assertTrue((np.array([[-5, 0, 2, 23], [-9, -4, 2, 3]]) == arr).all())


if __name__ == '__main__':
    unittest.main()
