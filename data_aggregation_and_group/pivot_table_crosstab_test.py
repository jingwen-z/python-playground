#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd

DF = pd.DataFrame({'Sample': range(1, 11),
                   'Nationality': ['USA', 'Japan', 'USA', 'Japan', 'Japan',
                                   'USA', 'Japan', 'USA', 'USA', 'USA'],
                   'Handedness': ['Right-handed', 'Left-handed', 'Right-handed',
                                  'Left-handed', 'Left-handed', 'Right-handed',
                                  'Left-handed', 'Left-handed', 'Right-handed',
                                  'Right-handed']},
                  columns=['Sample', 'Nationality', 'Handedness'])


class TestCrossTabulations(unittest.TestCase):
    def test_crosstab(self):
        result = pd.crosstab(DF['Nationality'], DF['Handedness'])
        expected = pd.pivot_table(DF, values='Sample', columns='Handedness',
                                  index='Nationality', aggfunc='count',
                                  fill_value=0)
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
