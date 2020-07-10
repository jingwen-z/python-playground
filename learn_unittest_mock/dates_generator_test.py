import unittest
from datetime import datetime, date
from unittest.mock import patch

import learn_unittest_mock.dates_generator as target

d_20191231 = datetime(2019, 12, 31)
d_20200101 = datetime(2020, 1, 1)
d_20200302 = datetime(2020, 3, 2)


class DatesGeneratorTest(unittest.TestCase):
    def setUp(self):
        # mock datetime to control today's date
        self.patcher = patch('learn_unittest_mock.dates_generator.datetime')
        self.patcher.start()

    def test_20191231(self):
        target.datetime.now.return_value = d_20191231
        self.assertEqual(d_20191231, target.datetime.now())

        res = target.start_end_dates()
        self.assertEqual(date(2019, 12, 23), res.last_week_start)
        self.assertEqual(date(2019, 12, 29), res.last_week_end)
        self.assertEqual(date(2019, 11, 1), res.last_month_start)
        self.assertEqual(date(2019, 11, 30), res.last_month_end)

    def test_20200101(self):
        target.datetime.now.return_value = d_20200101
        self.assertEqual(d_20200101, target.datetime.now())

        res = target.start_end_dates()
        self.assertEqual(date(2019, 12, 23), res.last_week_start)
        self.assertEqual(date(2019, 12, 29), res.last_week_end)
        self.assertEqual(date(2019, 12, 1), res.last_month_start)
        self.assertEqual(date(2019, 12, 31), res.last_month_end)

    def test_20200302(self):
        target.datetime.now.return_value = d_20200302
        self.assertEqual(d_20200302, target.datetime.now())

        res = target.start_end_dates()
        self.assertEqual(date(2020, 2, 24), res.last_week_start)
        self.assertEqual(date(2020, 3, 1), res.last_week_end)
        self.assertEqual(date(2020, 2, 1), res.last_month_start)
        self.assertEqual(date(2020, 2, 29), res.last_month_end)

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
