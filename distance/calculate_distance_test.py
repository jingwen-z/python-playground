# -*- coding: utf-8 -*-

import distance.calculate_distance as target
import unittest
import pandas as pd


class TestCalculateDistance(unittest.TestCase):
    def test_complete_zipcode(self):
        self.assertEqual('02700', target.complete_zipcode(2700))
        self.assertEqual('00520', target.complete_zipcode(520))
        self.assertEqual('75012', target.complete_zipcode(75012))

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

    @unittest.skip("Depends on time.")
    def test_get_itinerary(self):
        self.assertEqual([22.0, 36], target.get_itinerary(48.873481, 2.482640, 48.844172, 2.330246, 'NON'))

    def test_is_alternative(self):
        df1 = pd.DataFrame({'employee_id': ['10161', '10162'],
                            'employee_lat': [48.8734807, 49.6566844],
                            'employee_lng': [2.4826398, 3.3228483],
                            'itinerary_distance_km': [12.86, 2.088]})
        df2 = pd.DataFrame({'store_id': ['5578', '5579'],
                            'store_lat': [48.7946236, 48.8378712],
                            'store_lng': [2.3648647, 2.4832616]})
        self.assertTrue(target.is_alternative(df1, df2, 0, 1, 1.2))
        self.assertFalse(target.is_alternative(df1, df2, 1, 1, 1.2))


if __name__ == '__main__':
    unittest.main()
