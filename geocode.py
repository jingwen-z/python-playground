import requests
from urllib.parse import urlencode


def get_url(params, url='https://maps.googleapis.com/maps/api/geocode/json?'):
    return url + urlencode(params)


def get_formatted_address(json):
    if json['status'] == 'OK':
        return json['results'][0]['formatted_address']
    return 'Not found.'


def main():
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?' + urlencode(
            {'address': '1000000 rue adkfl', 'sensor': 'false'}))

    resp_json_payload = response.json()
    print('full json:')
    print(resp_json_payload)
    print('formatted addr:')
    print(get_formatted_address(resp_json_payload))


if __name__ == '__main__':
    main()
