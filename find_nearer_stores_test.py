# -*- coding: utf-8 -*-

import find_nearer_stores as target
import unittest


class TestFindNearerStores(unittest.TestCase):
    def test_complete_zipcode(self):
        self.assertEqual('02700', target.complete_zipcode('2700'))
        self.assertEqual('00520', target.complete_zipcode('520'))
        self.assertEqual('75012', target.complete_zipcode('75012'))

    def test_get_valid_addr(self):
        self.assertEqual('RUE A 75012', target.get_valid_addr(float('nan'), 'RUE A', '75012'))
        self.assertEqual('RUE A 75012', target.get_valid_addr(0, 'RUE A', '75012'))
        self.assertEqual('7-9 RUE A 75012', target.get_valid_addr(7.0, '9 RUE A', '75012'))
        self.assertEqual('7-9 RUE A 75012', target.get_valid_addr(7, 'A 9 RUE A', '75012'))
        self.assertEqual('7 RUE A 75012', target.get_valid_addr(7, 'RUE A', '75012'))

    @unittest.skip("Avoid sending requests in CI.")
    def test_geocode(self):
        self.assertEqual(
            [37.4216548, -122.0856374, 'Google Bldg 42, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA'],
            target.geocode('1600 Amphitheatre Parkway, Mountain View, CA'))
        self.assertEqual(['Latitude is not found', 'Longitude is not found', '1000000 rue adkfl'],
                         target.geocode('1000000 rue adkfl'))
        self.assertEqual(37.4216548, target.geocode('1600 Amphitheatre Parkway, Mountain View, CA')[0])


if __name__ == '__main__':
    unittest.main()
