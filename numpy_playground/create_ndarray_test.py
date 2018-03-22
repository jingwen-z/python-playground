#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestCreationNdarray(unittest.TestCase):
    def test_ndarray(self):
        data1 = [6, 7.5, 8, 0, 1]
        arr1 = np.array(data1)
        self.assertEqual((5,), arr1.shape)


if __name__ == '__main__':
    unittest.main()
