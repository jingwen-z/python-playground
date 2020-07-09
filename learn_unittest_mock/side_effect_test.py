import unittest
from unittest.mock import Mock

import requests
from requests.exceptions import Timeout

requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestSideEffect(unittest.TestCase):
    def test_side_effect(self):
        mock = Mock()
        mock.side_effect = [3, 2, 1]
        self.assertEqual(3, mock())
        self.assertEqual(2, mock())
        self.assertEqual(1, mock())

    def test_get_holiday_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holiday_timeout_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'key1': 'value1', 'key2': 'value2'}

        requests.get.side_effect = [Timeout, response_mock]
        with self.assertRaises(Timeout):
            get_holidays()

        self.assertEqual('value1', get_holidays()['key1'])


if __name__ == '__main__':
    unittest.main()
