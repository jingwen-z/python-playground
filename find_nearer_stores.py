# -*- coding: utf-8 -*-

import pandas as pd
import os

__author__ = 'Jingwen ZHENG'

WORK_DIR = '/Users/jingwen/Documents/R/datasets/understaffing-overstaffing'


def complete_zipcode(zipcode):
    if len(zipcode) == 1:
        zipcode = zipcode
    else:
        rep_time = 5 - len(zipcode)
        zipcode = '%s%s' % ('0' * rep_time, zipcode)
    return zipcode


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
                       columns={'Etablissement': 'storeId',
                                'Convention': 'storeConvention',
                                'e_norue': 'storeAddrNo',
                                'e_rue': 'storeAddr',
                                'e_postal': 'storeZipcode'})

    overstf_df.rename(index=str, inplace=True,
                      columns={'Matricule': 'employeeId',
                               'Numero de la rue salarié': 'employeeAddrNo',
                               'Nom de la rue salarié': 'employeeAddr',
                               'Code postal salarié': 'employeeZipcode',
                               'Etablissement': 'storeId',
                               'Convention': 'storeConvention',
                               'e_norue': 'storeAddrNo',
                               'e_rue': 'storeAddr',
                               'e_postal': 'storeZipcode',
                               'Titre de transport ?': 'byTransit'})

    print('understfDF:')
    print(understf_df.head())
    print('overstfDF:')
    print(overstf_df.head())

    understf_df['storeAddrNo'] = understf_df['storeAddrNo'].astype(object)
    overstf_df['employeeAddrNo'] = overstf_df['employeeAddrNo'].astype(object)
    overstf_df['storeAddrNo'] = overstf_df['storeAddrNo'].astype(object)

    understf_df['storeZipcode'] = understf_df['storeZipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['employeeZipcode'] = overstf_df['employeeZipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['storeZipcode'] = overstf_df['storeZipcode'].apply(lambda x: complete_zipcode(str(x)))

    print('understf - storeAddrNo isnull amount:')
    print(sum(pd.isnull(understf_df['storeAddrNo'])))
    print(pd.isnull(understf_df['storeAddrNo']))

    print('overstf_df - employeeAddrNo isnull amount:')
    print(sum(pd.isnull(overstf_df['employeeAddrNo'])))
    print(pd.isnull(overstf_df['employeeAddrNo']))

    print('overstf_df - storeAddrNo isnull amount:')
    print(sum(pd.isnull(overstf_df['storeAddrNo'])))
    print(pd.isnull(overstf_df['storeAddrNo']))


if __name__ == '__main__':
    main()
