#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
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
GRP_DF = DF.groupby(['day', 'smoker'])


class TestDataAggregation(unittest.TestCase):
    def test_multi_functions(self):
        result = GRP_DF['tip_pct'].agg(['mean', 'std'])

        self.assertEqual(result.columns[0], 'mean')
        self.assertEqual(result.columns[1], 'std')

    def test_column_wise(self):
        result = GRP_DF['tip_pct'].agg([('foo', 'mean'), ('bar', np.std)])

        self.assertEqual(result.columns[0], 'foo')
        self.assertTrue((result.loc[['Fri', 'Yes'], 'foo'] == 0.1 / 1).all())

    def test_list_functions(self):
        result = GRP_DF['tip_pct', 'total_bill'].agg(['count', 'mean', 'max'])

        self.assertEqual(result.columns[0], ('tip_pct', 'count'))
        self.assertEqual(result.columns[2], ('tip_pct', 'max'))
        self.assertEqual(result.columns[4], ('total_bill', 'mean'))

    def test_agg_Dict(self):
        result = GRP_DF.agg({'tip': np.max, 'size': 'sum'})
        expected_tip = max(
            (DF[(DF['day'] == 'Sun') & (DF['smoker'] == 'No')])['tip'])
        expected_size = sum(
            (DF[(DF['day'] == 'Sun') & (DF['smoker'] == 'No')])['size'])

        self.assertEqual(result['tip'][('Sun', 'No')], expected_tip)
        self.assertEqual(result['size'][('Sun', 'No')], expected_size)

    def test_agg_wo_row_idx(self):
        result = DF.groupby(['day', 'smoker'], as_index=False).mean()
        expected = DF.groupby(['day', 'smoker']).mean().reset_index()
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
