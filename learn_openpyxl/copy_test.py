import unittest

import openpyxl
import pandas as pd


class OpenpyxlTests(unittest.TestCase):
    def test_append(self):
        df1 = pd.DataFrame({'col1': ['cell1']})
        df1.to_excel('copy_test_df.xlsx', sheet_name='test', index=False)

        wb = openpyxl.load_workbook('copy_test_df.xlsx')
        ws_test = wb['test']
        self.assertEqual(ws_test['A2'].value, 'cell1')
        self.assertEqual(ws_test['B7'].value, None)

        df2 = pd.DataFrame({'col2': ['cell2']})
        writer = pd.ExcelWriter('copy_test_df.xlsx',
                                engine='openpyxl')
        writer.book = wb
        writer.sheets = {ws_test.title: ws_test}
        df2.to_excel(writer, sheet_name='test',
                     startrow=5, startcol=1, index=False)
        writer.save()

        wb = openpyxl.load_workbook('copy_test_df.xlsx')
        ws_test = wb['test']
        self.assertEqual(ws_test['A2'].value, 'cell1')
        self.assertEqual(ws_test['B7'].value, 'cell2')


if __name__ == '__main__':
    unittest.main()
