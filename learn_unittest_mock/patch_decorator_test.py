# If you want to mock an object for the duration of your entire test function,
# you can use patch() as a function decorator.

import unittest
from unittest.mock import patch

from learn_mock import get_holidays
from requests.exceptions import Timeout


class PatchDecoratorTest(unittest.TestCase):
    @patch('learn_mock.requests')
    def test_get_holiday(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

        mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
