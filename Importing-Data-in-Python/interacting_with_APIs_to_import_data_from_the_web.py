"""
Interacting with APIs to import data from the web
"""

import json
import requests

"""
Introduction to APIs and JSONs
"""

# Loading and exploring a JSON
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

"""
APIs and interacting with the world wide web
"""

# API requests
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

r = requests.get(url)
print(r.text)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

# Checking out the Wikipedia API
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

r = requests.get(url)
json_data = r.json()

pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
