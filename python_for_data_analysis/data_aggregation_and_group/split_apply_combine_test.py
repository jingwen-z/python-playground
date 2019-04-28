#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import pandas as pd

DF = pd.DataFrame({'total_bill': [10, 40, 20, 21, 19],
                   'tip': [1, 3, 2, 1.4, 1.9],
                   'smoker': ['No', 'No', 'Yes', 'No', 'Yes'],
                   'day': ['Sun', 'Mon', 'Fri', 'Sun', 'Tue'],
                   'time': ['Dinner'] * 5,
                   'size': [2, 3, 4, 3, 2],
                   'tip_pct': [0.1, 0.075, 0.1, 0.07, 0.1]},
                  columns=['total_bill', 'tip', 'smoker', 'day',
                           'time', 'size', 'tip_pct'])


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]


class TestSplitApplyCombine(unittest.TestCase):
    def test_grpby_apply(self):
        result = DF.groupby(['smoker', 'day']).apply(top, n=1,
                                                     column='total_bill')
        expected_p1 = DF[(DF['smoker'] == 'No') & (DF['day'] == 'Sun')]
        expected = expected_p1.sort_values(by='total_bill', ascending=False)

        self.assertEqual(result.loc[('No', 'Sun', 3), 'total_bill'],
                         expected.iloc[0, 0])

    def test_suppress_grp_keys(self):
        result = DF.groupby('smoker', group_keys=False).apply(top)
        self.assertTrue((result.index == [3, 1, 0, 2, 4]).all())
        self.assertTrue((result.columns == ['total_bill', 'tip', 'smoker',
                                            'day', 'time', 'size',
                                            'tip_pct']).all())


if __name__ == '__main__':
    unittest.main()
