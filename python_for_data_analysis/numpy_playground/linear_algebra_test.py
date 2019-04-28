#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestLinearAlgebra(unittest.TestCase):
    def test_dot(self):
        x = np.array([[2, 3], [5, 1], [2, 7]])
        y = np.array([[1, 3, 8], [9, 0, 2]])
        self.assertTrue((np.array([[29, 6, 22], [14, 15, 42], [65, 6, 30]]) == x.dot(y)).all())
        self.assertTrue((np.dot(x, y) == x.dot(y)).all())

    def test_infix_operator(self):
        x = np.array([[2, 3], [5, 1], [2, 7]])
        self.assertTrue((np.dot(x, np.ones(2)) == np.array([5, 6, 9])).all())
        self.assertTrue((np.dot(x, np.ones(2)) == x @ np.ones(2)).all())


if __name__ == '__main__':
    unittest.main()
