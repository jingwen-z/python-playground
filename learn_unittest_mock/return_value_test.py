import unittest
from datetime import datetime
from unittest.mock import Mock


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


tuesday = datetime(2020, 6, 30)
sunday = datetime(2020, 7, 5)

# Mock datetime to control today's date
datetime = Mock()


class ReturnValueTests(unittest.TestCase):
    def test_set_return_value_1(self):
        mock = Mock()
        mock.return_value = 7
        self.assertEqual(7, mock())

    def test_set_return_value_2(self):
        # the return value can also be set in the constructor
        mock = Mock(return_value=7)
        self.assertEqual(7, mock())

    def test_is_weekday_tuesday(self):
        datetime.today.return_value = tuesday
        self.assertTrue(is_weekday())

    def test_is_weekday_sunday(self):
        datetime.today.return_value = sunday
        self.assertFalse(is_weekday())


if __name__ == '__main__':
    unittest.main()
