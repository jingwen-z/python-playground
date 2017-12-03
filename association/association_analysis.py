# -*- coding: utf-8 -*-


import time

import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

COLUMN = 1


def mark(df):
    """
    Marks rows to drop in the given data-frame.

    :param df: data-frame to clean
    :return: a list of indexes to drop
    """
    # (k, v): (transaction_id, list(index))
    tx_map = {}
    to_drop = set()
    for row in df.itertuples():
        key = row.tx_id
        tx_map.setdefault(key, [])
        tx_map[key].append(row.Index)

    for indexes in tx_map.values():
        if len(indexes) == 1:
            to_drop.add(indexes[0])
    return to_drop


def clean(df):
    to_drop = mark(df)
    df.drop(to_drop, inplace=True)


def association_matrix(pivot_table):
    shelves = list(pivot_table.columns.values)
    df = pd.DataFrame(None, index=shelves, columns=shelves)

    frequent_item = apriori(pivot_table, min_support=0, use_colnames=True, max_len=2)
    rules = association_rules(frequent_item, metric="confidence", min_threshold=0)
    rules.sort_values(by=['antecedants', 'consequents'], kind='mergesort', inplace=True)

    for row in rules.itertuples():
        r = ', '.join(row.antecedants)
        c = ', '.join(row.consequents)
        df.loc[r, c] = row.confidence
    return df


def track(start, msg):
    total = time.time() - start
    print("Total %fs: %s" % (total, msg))


def main():
    start = time.time()

    df = pd.read_csv('tickets.csv', encoding='UTF-8', sep=';')
    df.rename(inplace=True, columns={'transactionId': 'tx_id', 'rayon': 'shelf', 'volume': 'amount'})
    track(start, 'CSV loaded')

    clean(df)
    track(start, 'cleaning DF finished')

    df.to_csv('multi_dept.csv', encoding='UTF-8', sep=';', index=False)
    track(start, 'CSV exported')

    pv_table = pd.pivot_table(df, values='amount', index=['tx_id'], columns=['shelf'], aggfunc=np.sum)
    pv_table.to_csv('dept_pivot_table.csv', encoding='UTF-8', sep=';', index=False)

    pv_table = pv_table.applymap(lambda x: 1 if x > 0 else 0)
    track(start, 'pivot table is ready')

    asso_mx = association_matrix(pv_table)
    asso_mx.to_csv('association_matrix.csv', encoding='UTF-8', sep=';')
    track(start, 'done')


if __name__ == '__main__':
    main()
