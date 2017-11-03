# -*- coding: utf-8 -*-

import geocode as target
import unittest


class TestGeocode(unittest.TestCase):
    def test_get_url(self):
        self.assertEqual('api?key=A+B+C', target.get_url({'key': 'A B C'}, url='api?'))


if __name__ == '__main__':
    unittest.main()
