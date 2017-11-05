# -*- coding: utf-8 -*-

import math
import os
import pandas as pd
import re
import requests
from urllib.parse import urlencode

__author__ = 'Jingwen ZHENG'

WORK_DIR = '/Users/jingwen/Documents/python/datasets/understaffing_overstaffing'
STARTS_WITH_DIGIT = re.compile('^\\d.*')
STARTS_WITH_A = re.compile('^A .*')


def complete_zipcode(zipcode):
    if len(zipcode) == 1:
        zipcode = zipcode
    else:
        rep_time = 5 - len(zipcode)
        zipcode = '%s%s' % ('0' * rep_time, zipcode)
    return zipcode


def get_valid_addr(nb, road, zipcode):
    """
    Get valid address

    :param nb: number of type float64, can be NaN
    """
    if math.isnan(nb) or nb == 0:
        return '%s %s' % (road, zipcode)
    if STARTS_WITH_DIGIT.match(road):
        return '%s-%s %s' % (int(nb), road, zipcode)
    if STARTS_WITH_A.match(road):
        return '%s-%s %s' % (int(nb), road[2:], zipcode)
    return '%s %s %s' % (int(nb), road, zipcode)


def geocode(address):
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?' + urlencode({'address': address, 'sensor': 'false'}))
    resp_address = response.json()

    if resp_address['status'] == 'OK':
        lat = resp_address['results'][0]['geometry']['location']['lat']
        lng = resp_address['results'][0]['geometry']['location']['lng']
        formatted_addr = resp_address['results'][0]['formatted_address']
        return [lat, lng, formatted_addr]
    else:
        print('Failed to get json response:', resp_address)
        return ['Latitude is not found', 'Longitude is not found', address]


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

    understf_df['store_zipcode'] = understf_df['store_zipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['employee_zipcode'] = overstf_df['employee_zipcode'].apply(lambda x: complete_zipcode(str(x)))
    overstf_df['store_zipcode'] = overstf_df['store_zipcode'].apply(lambda x: complete_zipcode(str(x)))

    print('understf - store_addr_no isnull amount:')
    print(sum(pd.isnull(understf_df['store_addr_no'])))

    print('overstf_df - employee_addr_no isnull amount:')
    print(sum(pd.isnull(overstf_df['employee_addr_no'])))

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

    for i, cols in understf_df.iterrows():
        addr_cmpl = get_valid_addr(cols.store_addr_no,
                                   cols.store_addr,
                                   cols.store_zipcode)
        understf_df.set_value(i, 'store_addr_cmpl', addr_cmpl)

    for i, cols in overstf_df.iterrows():
        empl_addr_cmpl = get_valid_addr(cols.employee_addr_no,
                                        cols.employee_addr,
                                        cols.employee_zipcode)
        overstf_df.set_value(i, 'employee_addr_cmpl', empl_addr_cmpl)

        store_addr_cmpl = get_valid_addr(cols.store_addr_no,
                                         cols.store_addr,
                                         cols.store_zipcode)
        overstf_df.set_value(i, 'store_addr_cmpl', store_addr_cmpl)

    for i, cols in understf_df.iterrows():
        if understf_df.loc[i, 'store_lat'] is None:
            loc_store = geocode(understf_df.loc[i, 'store_addr_cmpl'])
            understf_df.set_value(i, 'store_lat', loc_store[0])
            understf_df.set_value(i, 'store_lng', loc_store[1])
            understf_df.set_value(i, 'store_addr_cmpl', loc_store[2])
            print(i)
        else:
            print(understf_df['store_id'])

    print('first 5 rows of understfDF:')
    print(understf_df.head(5))

    understf_df.to_csv('understf_coordinate.csv', encoding='ISO-8859-1', sep=';')

    for i, cols in overstf_df.iterrows():
        if overstf_df.loc[i, 'store_lat'] is None:
            loc_store = geocode(overstf_df.loc[i, 'store_addr_cmpl'])
            overstf_df.set_value(i, 'store_lat', loc_store[0])
            overstf_df.set_value(i, 'store_lng', loc_store[1])
            overstf_df.set_value(i, 'store_addr_cmpl', loc_store[2])
            print(i)
        else:
            print(overstf_df['store_id'])

    for i, cols in overstf_df.iterrows():
        if overstf_df.loc[i, 'employee_lat'] is None:
            loc_empl = geocode(overstf_df.loc[i, 'employee_addr_cmpl'])
            overstf_df.set_value(i, 'employee_lat', loc_empl[0])
            overstf_df.set_value(i, 'employee_lng', loc_empl[1])
            overstf_df.set_value(i, 'employee_addr_cmpl', loc_empl[2])
            print(i)
        else:
            print(overstf_df['employee_id'])

    print('first 5 rows of overstfDF:')
    print(overstf_df.head(5))

    overstf_df.to_csv('overstf_coordinate.csv', encoding='UTF-8', sep=';')


if __name__ == '__main__':
    main()
