#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

ARR = np.array([2, 4, 6])


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertTrue((np.array([3, 5, 7]) == ARR + 1).all())

    def test_subtraction(self):
        self.assertTrue((np.array([1, 3, 5]) == ARR - 1).all())

    def test_multiply(self):
        self.assertTrue((np.array([4, 16, 36]) == ARR * ARR).all())

    def test_division(self):
        self.assertTrue((np.array([1, 2, 3]) == ARR / 2).all())

    def test_square(self):
        self.assertTrue((np.array([4, 16, 36]) == ARR ** 2).all())


if __name__ == '__main__':
    unittest.main()
