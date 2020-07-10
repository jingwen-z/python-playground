from urllib.parse import urlencode

import requests


class Place:
    def __init__(self, lat, lng, place_name, place_id, glb_rating):
        self.lat = lat
        self.lng = lng
        self.place_name = place_name
        self.place_id = place_id
        self.glb_rating = glb_rating


def search_place(gps='gps', api_key='api_key') -> Place:
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' + urlencode(
            {'location': gps, 'rankby': 'distance',
             'name': 'La Poste', 'key': api_key}
        ))

    if response.status_code == 200:
        resp_json = response.json()
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
        place_name = resp_json['results'][0]['name']
        place_id = resp_json['results'][0]['place_id']
        glb_rating = resp_json['results'][0]['rating']
        return Place(lat, lng, place_name, place_id, glb_rating)
    else:
        return Place(0, 0, 'null', 'null', 0)
