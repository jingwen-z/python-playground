#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestCreationNdarray(unittest.TestCase):
    def test_ndarray(self):
        data = np.random.randn(2, 3)
        print(data)


if __name__ == '__main__':
    unittest.main()
