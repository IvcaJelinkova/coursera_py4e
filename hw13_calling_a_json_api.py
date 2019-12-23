# hw13_calling_a_json_api.py

# The program will prompt for a location, contact a web service and retrieve JSON
# for the web service and parse that data, and retrieve the first place_id from
# the JSON. A place ID is a textual identifier that uniquely identifies a place
# as within Google Maps.

# API End Points: http://py4e-data.dr-chuck.net/json?

import urllib.request, urllib.parse, urllib.error
import json

api_key = False
if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        address = 'South Federal University' # place_id = "ChIJNeHD4p-540AR2Q0_ZjwmKJ8

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print('Retrieving', len(data), 'characters. ')
    #print(data)

    js = json.loads(data)
    #print('\n', json.dumps(js))

    place_id = js['results'][0]['place_id']
    print('==========im here!!! Place_id:', place_id)


