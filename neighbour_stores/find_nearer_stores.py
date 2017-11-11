# -*- coding: utf-8 -*-

import configparser
import math
import os
import re
from urllib.parse import urlencode

import pandas as pd
import requests

__author__ = 'Jingwen ZHENG'

WORK_DIR = '/Users/jingwen/Documents/python/datasets/understaffing_overstaffing'
STARTS_WITH_DIGIT = re.compile('^\\d.*')
STARTS_WITH_A = re.compile('^A .*')


def complete_zipcode(zipcode):
    """
    :type zipcode: int
    :param zipcode: incomplete zipcode
    :return: a completed zipcode as string in 5 characters
    """
    return ('00000%d' % zipcode)[-5:]


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


def get_itinerary(origin_lat, origin_lng, dest_lat, dest_lng, by_transit):
    config = configparser.ConfigParser()
    config.read('/Users/jingwen/Documents/python/global_key.properties')
    key = config['google']['python.playground']

    origin = '%f, %f' % (origin_lat, origin_lng)
    destination = '%f, %f' % (dest_lat, dest_lng)

    if by_transit == 'OUI':
        mode = 'transit'
    else:
        mode = 'driving'

    response = requests.get(
        'https://maps.googleapis.com/maps/api/distancematrix/json?language=en&' +
        urlencode({'origins': origin,
                   'destinations': destination,
                   'mode': mode,
                   'key': key}))
    distance_info = response.json()

    try:
        if distance_info['rows'][0]['elements'][0]['status'] == 'OK':
            duration = distance_info['rows'][0]['elements'][0]['duration']['text'][:-5]
            distance = distance_info['rows'][0]['elements'][0]['distance']['text'][:-3]
            return [duration, distance]
        else:
            print('Failed to get correct response:', response)
    except IndexError:
        print('Failed to get status, response:', distance_info)
        raise


def create_tgt_df(filename):
    """
    :param filename: name of related file to import
    """
    df = pd.read_csv(filename, encoding='ISO-8859-1', sep=';')

    df = df[['Etablissement', 'Convention', 'e_norue', 'e_rue', 'e_postal']]
    df.rename(index=str, inplace=True,
              columns={'Etablissement': 'store_id',
                       'Convention': 'store_convention',
                       'e_norue': 'store_addr_no',
                       'e_rue': 'store_addr',
                       'e_postal': 'store_zipcode'})

    df['store_zipcode'] = df['store_zipcode'].apply(lambda x: complete_zipcode(x))

    df['store_addr_cmpl'] = None
    df['store_lat'] = None
    df['store_lng'] = None

    for i, cols in df.iterrows():
        address = get_valid_addr(cols.store_addr_no,
                                 cols.store_addr,
                                 cols.store_zipcode)
        df.set_value(i, 'store_addr_cmpl', address)

    return df


def create_src_df(filename):
    """
    :param filename: name of related file to import
    """
    df = pd.read_csv(filename, encoding='ISO-8859-1', sep=';')

    df = df[['Matricule', 'Numero de la rue salarié', 'Nom de la rue salarié', 'Code postal salarié',
             'Etablissement', 'Convention', 'e_norue', 'e_rue', 'e_postal', 'Titre de transport ?']]
    df.rename(index=str, inplace=True,
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

    df['employee_zipcode'] = df['employee_zipcode'].apply(lambda x: complete_zipcode(x))
    df['store_zipcode'] = df['store_zipcode'].apply(lambda x: complete_zipcode(x))

    df.insert(loc=4, column='employee_addr_cmpl', value=None)
    df.insert(loc=5, column='employee_lat', value=None)
    df.insert(loc=6, column='employee_lng', value=None)
    df.insert(loc=12, column='store_addr_cmpl', value=None)
    df.insert(loc=13, column='store_lat', value=None)
    df.insert(loc=14, column='store_lng', value=None)

    for i, cols in df.iterrows():
        empl_addr = get_valid_addr(cols.employee_addr_no,
                                   cols.employee_addr,
                                   cols.employee_zipcode)
        df.set_value(i, 'employee_addr_cmpl', empl_addr)

        store_addr = get_valid_addr(cols.store_addr_no,
                                    cols.store_addr,
                                    cols.store_zipcode)
        df.set_value(i, 'store_addr_cmpl', store_addr)

    return df


def fill_tgt_coord(df, extra_file):
    for i, cols in df.iterrows():
        if df.loc[i, 'store_lat']:
            print(df['store_id'])
        else:
            loc_store = geocode(df.loc[i, 'store_addr_cmpl'])
            df.set_value(i, 'store_lat', loc_store[0])
            df.set_value(i, 'store_lng', loc_store[1])
            df.set_value(i, 'store_addr_cmpl', loc_store[2])
            print(i)

    extra_df = pd.read_csv(extra_file, encoding='ISO-8859-1', sep=',')

    if extra_df['df'] == 'tgt_store_df' and extra_df['subject'] == 'store':
        df.set_value(extra_df['id'], 'store_lat', extra_df['latitude'])
        df.set_value(extra_df['id'], 'store_lng', extra_df['longitude'])
        df.set_value(extra_df['id'], 'store_addr_cmpl', extra_df['address'])


def fill_src_coord(df, extra_file):
    for i, cols in df.iterrows():
        if df.loc[i, 'store_lat']:
            print(df['store_id'])
        else:
            location = geocode(df.loc[i, 'store_addr_cmpl'])
            df.set_value(i, 'store_lat', location[0])
            df.set_value(i, 'store_lng', location[1])
            df.set_value(i, 'store_addr_cmpl', location[2])
            print(i)

    for i, cols in df.iterrows():
        if df.loc[i, 'employee_lat']:
            print(df['employee_id'])
        else:
            location = geocode(df.loc[i, 'employee_addr_cmpl'])
            df.set_value(i, 'employee_lat', location[0])
            df.set_value(i, 'employee_lng', location[1])
            df.set_value(i, 'employee_addr_cmpl', location[2])
            print(i)

    extra_df = pd.read_csv(extra_file, encoding='ISO-8859-1', sep=',')

    if extra_df['df'] == 'src_empl_df' and extra_df['subject'] == 'store':
        df.set_value(extra_df['id'], 'store_addr_cmpl', extra_df['address'])
        if extra_df['id'] != 3 and extra_df['id'] != 269:
            df.set_value(extra_df['id'], 'store_lat', extra_df['latitude'])
            df.set_value(extra_df['id'], 'store_lng', extra_df['longitude'])

    if extra_df['df'] == 'src_empl_df' and extra_df['subject'] == 'employee':
        df.set_value(extra_df['id'], 'employee_lat', extra_df['latitude'])
        df.set_value(extra_df['id'], 'employee_lng', extra_df['longitude'])
        df.set_value(extra_df['id'], 'employee_addr_cmpl', extra_df['address'])


def actual_itinerary(df):
    df.insert(loc=16, column='itinerary_duration_minute', value=None)
    df.insert(loc=17, column='itinerary_distance_km', value=None)
    df.insert(loc=18, column='itinerary_distance_haversine_km', value=None)

    for i, cols in df.iterrows():
        itinerary = get_itinerary(df['employee_lat'][i], df['employee_lng'][i], df['store_lat'][i],
                                  df['store_lng'][i], df['by_transit'][i])
        df.set_value(i, 'itinerary_duration_minute', itinerary[0])
        df.set_value(i, 'itinerary_distance_km', itinerary[1])
        print(i)


def main():
    print('work directory=%s' % WORK_DIR)
    os.chdir(WORK_DIR)
    pd.options.display.max_colwidth = 100

    tgt_df = create_tgt_df('understaffing.csv')
    src_df = create_src_df('overstaffing.csv')

    fill_tgt_coord(tgt_df, 'complete_coordinates.csv')
    fill_src_coord(src_df, 'complete_coordinates.csv')

    src_df = src_df[(src_df['employee_id'] != '10104') & (src_df['employee_id'] != '44522')]

    tgt_df.to_csv('understf_coordinate.csv', encoding='ISO-8859-1', sep=';')
    src_df.to_csv('overstf_coordinate.csv', encoding='ISO-8859-1', sep=';')

    actual_itinerary(src_df)


if __name__ == '__main__':
    main()
