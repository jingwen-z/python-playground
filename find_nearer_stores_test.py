# -*- coding: utf-8 -*-

import find_nearer_stores as target
import unittest


class TestFindNearerStores(unittest.TestCase):
    def test_complete_zipcode(self):
        self.assertEqual(target.complete_zipcode('2700'), '02700')
        self.assertEqual(target.complete_zipcode('520'), '00520')
        self.assertEqual(target.complete_zipcode('75012'), '75012')


if __name__ == '__main__':
    unittest.main()
