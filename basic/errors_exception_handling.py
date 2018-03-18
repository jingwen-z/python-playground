#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest


class TestErrorException(unittest.TestCase):
    def bad_example(self):
        raise Exception('Broken')

    def attempt_float_1(self, x):
        try:
            return float(x)
        except ValueError:
            return 'ValueError'

    def attempt_float_2(self, x):
        try:
            return float(x)
        except (ValueError, TypeError):
            return 'ValueError or TypeError'

    def test_raise_exception(self):
        self.assertRaises(Exception, self.bad_example)

    def test_catch_valueerror(self):
        self.assertEqual(1.2, self.attempt_float_1('1.2'))
        self.assertEqual('ValueError', self.attempt_float_1('something'))

    def test_catch_multi_error(self):
        self.assertEqual('ValueError or TypeError', self.attempt_float_2((1, 2)))


if __name__ == '__main__':
    unittest.main()
