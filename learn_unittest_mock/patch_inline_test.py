import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

import learn_unittest_mock.learn_mock


class PatchInlineTest(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('learn_unittest_mock.learn_mock.requests')
        self.patcher.start()

    def test_get_holiday(self):
        learn_unittest_mock.learn_mock.requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            learn_unittest_mock.learn_mock.get_holidays()

        learn_unittest_mock.learn_mock.requests.get.assert_called_once()

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
