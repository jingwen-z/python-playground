import unittest
from unittest.mock import patch, Mock, call

from requests.exceptions import Timeout

import learn_unittest_mock.google_place_api as target


class GooglePlaceApiTest(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('learn_unittest_mock.google_place_api.requests')
        self.patcher.start()

    def test_search_place_side_effect(self):
        target.requests.get.side_effect = Timeout

        # use .assertRaises() to verify that get_holidays() raises an exception
        # given the new side effect of get()
        with self.assertRaises(Timeout):
            target.search_place()

    def test_search_place_return_value(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            'results': [
                {
                    'geometry': {
                        'location': {
                            'lat': 48.830273,
                            'lng': 2.8059952
                        }
                    },
                    'name': 'La Poste',
                    'place_id': 'abcdefg',
                    'rating': 5
                }
            ]
        }

        target.requests.get.side_effect = [Timeout, response_mock]
        with self.assertRaises(Timeout):
            target.search_place()

        res = target.search_place()

        # test requests' results
        self.assertEqual(res.lat, 48.830273)
        self.assertEqual(res.lng, 2.8059952)
        self.assertEqual(res.place_name, 'La Poste')
        self.assertEqual(res.place_id, 'abcdefg')
        self.assertEqual(res.glb_rating, 5)

        # assert that the mock was called at least once
        target.requests.get.assert_called()

        # how many times the mock object has been called
        self.assertEqual(2, target.requests.get.call_count)

        # test arguments that the mock was last called with
        self.assertEqual(
            call(
                'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=gps&rankby=distance&name=La+Poste&key=api_key'),
            target.requests.get.call_args)

        # list of all the calls made to the mock object in sequence
        self.assertEqual(
            [
                call(
                    'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=gps&rankby=distance&name=La+Poste&key=api_key'),
                call(
                    'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=gps&rankby=distance&name=La+Poste&key=api_key')],
            target.requests.get.call_args_list)

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
