# -*- coding: utf-8 -*-

import os
import pandas as pd
import re

__author__ = 'Jingwen ZHENG'

WORK_DIR = '/Users/jingwen/Documents/R/datasets/understaffing-overstaffing'


def complete_zipcode(zipcode):
    if len(zipcode) == 1:
        zipcode = zipcode
    else:
        rep_time = 5 - len(zipcode)
        zipcode = '%s%s' % ('0' * rep_time, zipcode)
    return zipcode


def get_valid_addr(addrNo, addrName, zipcode):
    pattern_dig = re.compile('^\\d.*')
    pattern_prep = re.compile('^A .*')

    startsWithDig = pattern_dig.match(addrName) is not None
    startsWithPrep = pattern_prep.match(addrName) is not None

    # pd.isnull(addrNo)

    if pd.isnull(addrNo) or addrNo == '0' or addrNo == '':
        return '%s %s' % (addrName, zipcode)
    if startsWithDig:
        return '%s-%s %s' % (addrNo, addrName, zipcode)
    if startsWithPrep:
        return '%s-%s %s' % (addrNo, addrName[2:50], zipcode)
    return '%s %s %s' % (addrNo, addrName, zipcode)


def main():
    print('work directory=%s' % WORK_DIR)
    os.chdir(WORK_DIR)

    """
    data preparation
    """
    understf_file = 'understaffing.csv'
    overstf_file = 'overstaffing.csv'

    understf_df = pd.read_csv(understf_file, encoding='ISO-8859-1', sep=';')
    overstf_df = pd.read_csv(overstf_file, encoding='ISO-8859-1', sep=';')

    """
    take useful fields
    """
    understf_df = understf_df[['Etablissement', 'Convention', 'e_norue', 'e_rue', 'e_postal']]
    overstf_df = overstf_df[['Matricule', 'Numero de la rue salarié', 'Nom de la rue salarié', 'Code postal salarié',
                             'Etablissement', 'Convention', 'e_norue', 'e_rue', 'e_postal', 'Titre de transport ?']]

    understf_df.rename(index=str, inplace=True,
                       columns={'Etablissement': 'store_id',
                                'Convention': 'store_convention',
                                'e_norue': 'store_addr_no',
                                'e_rue': 'store_addr',
                                'e_postal': 'store_zipcode'})

    overstf_df.rename(index=str, inplace=True,
                      columns={'Matricule': 'employee_id',
                               'Numero de la rue salarié': 'employee_addr_no',
                               'Nom de la rue salarié': 'employee_addr',
                               'Code postal salarié': 'employee_zipcode',
                               'Etablissement': 'store_id',
                               'Convention': 'store_convention',
                               'e_norue': 'store_addr_no',
                               'e_rue': 'store_addr',
                               'e_postal': 'store_zipcode',
                               'Titre de transport ?': 'by_transit'})

    # understf_df['store_addr_no'] = understf_df['store_addr_no'].astype(int)
    print(understf_df.dtypes)
    # overstf_df['employee_addr_no'] = overstf_df['employee_addr_no'].astype(object)
    # overstf_df['store_addr_no'] = overstf_df['store_addr_no'].astype(object)

    understf_df['store_zipcode'] = understf_df['store_zipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['employee_zipcode'] = overstf_df['employee_zipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['store_zipcode'] = overstf_df['store_zipcode'].apply(lambda x: complete_zipcode(str(x)))

    print('understf - store_addr_no isnull amount:')
    print(sum(pd.isnull(understf_df['store_addr_no'])))
    # print(pd.isnull(understf_df['store_addr_no']))

    print('overstf_df - employee_addr_no isnull amount:')
    print(sum(pd.isnull(overstf_df['employee_addr_no'])))
    # print(pd.isnull(overstf_df['employee_addr_no']))

    print('overstf_df - store_addr_no isnull amount:')
    print(sum(pd.isnull(overstf_df['store_addr_no'])))

    understf_df['store_addr_cmpl'] = None
    understf_df['store_lat'] = None
    understf_df['store_lng'] = None

    overstf_df.insert(loc=4, column='employee_addr_cmpl', value=None)
    overstf_df.insert(loc=5, column='employee_lat', value=None)
    overstf_df.insert(loc=6, column='employee_lng', value=None)
    overstf_df.insert(loc=12, column='store_addr_cmpl', value=None)
    overstf_df.insert(loc=13, column='store_lat', value=None)
    overstf_df.insert(loc=14, column='store_lng', value=None)

    print('------------------------')

    for i, cols in understf_df.iterrows():
        addr_cmpl = get_valid_addr(cols.store_addr_no,
                                   cols.store_addr,
                                   cols.store_zipcode)
        understf_df.set_value(i, 'store_addr_cmpl', addr_cmpl)

    print('understfDF:')
    print(understf_df.head())

    # print('understfDF - store_addr:')
    # print(understf_df['store_addr'][0])


if __name__ == '__main__':
    main()
