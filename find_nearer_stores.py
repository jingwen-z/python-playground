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
    pd.options.display.max_colwidth = 100

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

    """
    check missing coordinates
    """

    understf_file = 'understf_coordinate.csv'
    overstf_file = 'overstf_coordinate.csv'

    understf_df = pd.read_csv(understf_file, encoding='ISO-8859-1', sep=';')
    overstf_df = pd.read_csv(overstf_file, encoding='ISO-8859-1', sep=';')

    print('------------------ understf_df[\'store_lat\']----------------------')
    print('understf_df - data \'store_lat is not found\':')
    print(understf_df.loc[understf_df['store_lat'] == 'Latitude is not found'])
    print('------------------overstf_df[\'store_lat\']----------------------')
    print('overstf_df - data \'store_lat is not found\':')
    print(overstf_df.loc[overstf_df['store_lat'] == 'Latitude is not found'])
    print('------------------overstf_df[\'employee_lat\']----------------------')
    print('overstf_df - data \'employee_lat is not found\':')
    print(overstf_df.loc[overstf_df['employee_lat'] == 'Latitude is not found'])

    understf_df.set_value(43, 'store_lat', '43.3280423')
    understf_df.set_value(43, 'store_lng', '5.1495158')
    understf_df.set_value(43, 'store_addr_cmpl', '2 Chemin du Rivage, 13620 Carry-le-Rouet, France')
    print(understf_df.iloc[43, :])

    overstf_df.set_value(108, 'store_lat', '48.7773784')
    overstf_df.set_value(108, 'store_lng', '2.0047956')
    overstf_df.set_value(108, 'store_addr_cmpl', '36 Avenue Paul Vaillant-Couturier, 78190 Trappes, France')
    print('----------------- 108 --------------------')
    print(overstf_df.iloc[108, :])

    overstf_df.set_value(193, 'store_lat', '48.8347881')
    overstf_df.set_value(193, 'store_lng', '2.3198215')
    overstf_df.set_value(193, 'store_addr_cmpl', '53 Rue Raymond Losserand, 75014 Paris, France')
    print('----------------- 193 --------------------')
    print(overstf_df.iloc[193, :])

    overstf_df.set_value(209, 'store_lat', '48.8327632')
    overstf_df.set_value(209, 'store_lng', '2.2498996')
    overstf_df.set_value(209, 'store_addr_cmpl', '36 Rue du Dôme, 92100 Boulogne-Billancourt, France')
    print('----------------- 209 --------------------')
    print(overstf_df.iloc[209, :])

    overstf_df.set_value(210, 'store_lat', '48.8787391')
    overstf_df.set_value(210, 'store_lng', '2.370933')
    overstf_df.set_value(210, 'store_addr_cmpl', '9 Rue de Meaux, 75019 Paris, France')
    print('----------------- 210 --------------------')
    print(overstf_df.iloc[210, :])

    overstf_df.set_value(211, 'store_lat', '48.8505606')
    overstf_df.set_value(211, 'store_lng', '2.3899131')
    overstf_df.set_value(211, 'store_addr_cmpl', '63 Rue de Montreuil, 75011 Paris-11E-Arrondissement, France')
    print('----------------- 211 --------------------')
    print(overstf_df.iloc[211, :])

    overstf_df.set_value(271, 'store_lat', '48.9068377')
    overstf_df.set_value(271, 'store_lng', '2.1508612')
    overstf_df.set_value(271, 'store_addr_cmpl', 'Place Paul Démange, 78360 Montesson, France')
    print('----------------- 271 --------------------')
    print(overstf_df.iloc[271, :])

    overstf_df.set_value(282, 'store_lat', '48.8462586')
    overstf_df.set_value(282, 'store_lng', '2.3243925')
    overstf_df.set_value(282, 'store_addr_cmpl', '79 Rue de Vaugirard, 75006 Paris, France')
    print('----------------- 282 --------------------')
    print(overstf_df.iloc[282, :])

    overstf_df.set_value(3, 'employee_lat', '49.6566844')
    overstf_df.set_value(3, 'employee_lng', '3.3228483')
    overstf_df.set_value(3, 'employee_addr_cmpl', '57 Avenue André Boulloche, 02700 Tergnier, France')
    print('----------------- 3 --------------------')
    print(overstf_df.iloc[3, :])

    overstf_df.set_value(29, 'employee_lat', '48.9501867')
    overstf_df.set_value(29, 'employee_lng', '2.3395551')
    overstf_df.set_value(29, 'employee_addr_cmpl', '17 Rue Georges Thibout, 93800 Épinay-sur-Seine, France')
    print('----------------- 29 --------------------')
    print(overstf_df.iloc[29, :])

    overstf_df.set_value(111, 'employee_lat', '43.1375916')
    overstf_df.set_value(111, 'employee_lng', '6.0390838')
    overstf_df.set_value(111, 'employee_addr_cmpl', '215 Chemin Jules Fontan, 83130 La Garde, France')
    print('----------------- 111 --------------------')
    print(overstf_df.iloc[111, :])

    overstf_df.set_value(171, 'employee_lat', '48.9493912')
    overstf_df.set_value(171, 'employee_lng', '2.4407945')
    overstf_df.set_value(171, 'employee_addr_cmpl', 'Avenue Garros, 93150 Le Blanc-Mesnil, France')
    print('----------------- 171 --------------------')
    print(overstf_df.iloc[171, :])

    overstf_df.set_value(269, 'employee_lat', '48.9081922')
    overstf_df.set_value(269, 'employee_lng', '2.1524869')
    overstf_df.set_value(269, 'employee_addr_cmpl', '17 Rue Pierre Louis Guyard, 78360 Montesson, France')
    print('----------------- 269 --------------------')
    print(overstf_df.iloc[269, :])


    overstf_df.set_value(3, 'store_addr_cmpl', '1 Boulevard Gustave Grégoire, 02700 Tergnier, France')
    print('----------------- 3 --------------------')
    print(overstf_df.iloc[3, :])

    overstf_df.set_value(108, 'employee_lat', '48.7654636')
    overstf_df.set_value(108, 'employee_lng', '1.9493117')
    overstf_df.set_value(108, 'employee_addr_cmpl', '1 Allée du Théâtre, 78990 Élancourt, France')
    print('----------------- 108 --------------------')
    print(overstf_df.iloc[108, :])

    overstf_df.set_value(133, 'employee_lat', '43.463088')
    overstf_df.set_value(133, 'employee_lng', '5.231285')
    overstf_df.set_value(133, 'employee_addr_cmpl', 'Rue Louis Blériot, 13127 Vitrolles, France')
    print('----------------- 133 --------------------')
    print(overstf_df.iloc[133, :])

    overstf_df.set_value(165, 'employee_lat', '48.8537731')
    overstf_df.set_value(165, 'employee_lng', '2.3992899')
    overstf_df.set_value(165, 'employee_addr_cmpl', '27 Rue des Vignoles, 75020 Paris, France')
    print('----------------- 165 --------------------')
    print(overstf_df.iloc[165, :])

    overstf_df.set_value(214, 'employee_lat', '49.0521864')
    overstf_df.set_value(214, 'employee_lng', '2.0447988')
    overstf_df.set_value(214, 'employee_addr_cmpl', '20 Boulevard de la Paix, 95800 Cergy, France')
    print('----------------- 214 --------------------')
    print(overstf_df.iloc[214, :])

    overstf_df.set_value(269, 'store_addr_cmpl', 'Place Paul Démange, 78360 Montesson, France')
    print('----------------- 269 --------------------')
    print(overstf_df.iloc[269, :])

    overstf_df.set_value(231, 'employee_lat', '48.9659105')
    overstf_df.set_value(231, 'employee_lng', '2.5430213')
    overstf_df.set_value(231, 'employee_addr_cmpl', '5 Allée Antoine de Saint-Exupéry, 93420 Villepinte, France')
    print('----------------- 231 --------------------')
    print(overstf_df.iloc[231, :])

    overstf_df = overstf_df[(overstf_df['employee_id'] != '10104') & (overstf_df['employee_id'] != '44522')]
    print(overstf_df.shape)

    understf_df.to_csv('understf_coordinate.csv', encoding='ISO-8859-1', sep=';', index=False)
    overstf_df.to_csv('overstf_coordinate.csv', encoding='UTF-8', sep=';', index=False)

    """
    find nearer stores for staffs in overstaffed stores
    """

    overstf_df.insert(loc=16, column='itinerary_duration_minute', value=None)
    overstf_df.insert(loc=17, column='itinerary_distance_km', value=None)
    overstf_df.insert(loc=18, column='itinerary_disthav_km', value=None)

    print(overstf_df)


if __name__ == '__main__':
    main()
