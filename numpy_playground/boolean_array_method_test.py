#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestBoolArrayMethod(unittest.TestCase):
    def test_any(self):
        bools = np.array([False, False, True, False])
        self.assertTrue(bools.any())

    def test_all(self):
        bools = np.array([False, False, True, False])
        self.assertFalse(bools.all())


if __name__ == '__main__':
    unittest.main()
