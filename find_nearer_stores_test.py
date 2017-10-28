# -*- coding: utf-8 -*-

import find_nearer_stores as target
import unittest


class TestFindNearerStores(unittest.TestCase):
    def test_complete_zipcode(self):
        self.assertEqual('02700', target.complete_zipcode('2700'))
        self.assertEqual('00520', target.complete_zipcode('520'))
        self.assertEqual('75012', target.complete_zipcode('75012'))

    def test_get_valid_addr(self):
        self.assertEqual('RUE A 75012', target.get_valid_addr(None, 'RUE A', '75012', False, False))
        self.assertEqual('RUE A 75012', target.get_valid_addr('0', 'RUE A', '75012', False, False))
        self.assertEqual('RUE A 75012', target.get_valid_addr('', 'RUE A', '75012', False, False))
        self.assertEqual('7-9 RUE A 75012', target.get_valid_addr('7', '9 RUE A', '75012', True, False))
        self.assertEqual('7-9 RUE A 75012', target.get_valid_addr('7', 'A 9 RUE A', '75012', False, True))
        self.assertEqual('7 RUE A 75012', target.get_valid_addr('7', 'RUE A', '75012', False, False))

if __name__ == '__main__':
    unittest.main()
