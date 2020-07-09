import unittest
from unittest.mock import patch

import learn_mock
from learn_mock import get_holidays
from requests.exceptions import Timeout


class PatchInlineTest(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('learn_mock.requests')
        self.patcher.start()

    def test_get_holiday(self):
        learn_mock.requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

        learn_mock.requests.get.assert_called_once()

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
