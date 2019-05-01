# -*- coding: utf-8 -*-

import unittest

import pandas as pd

import association.association_analysis as target


class TestAssociationAnalysis(unittest.TestCase):
    def test_clean_rows(self):
        df = pd.DataFrame({'tx_id': ['1', '1', '3'],
                           'shelf': ['dA', 'dB', 'dC'],
                           'amount': [1, 2, 3]})
        target.clean(df)
        self.assertEqual([0, 1], df.index.values.tolist())


if __name__ == '__main__':
    unittest.main()
