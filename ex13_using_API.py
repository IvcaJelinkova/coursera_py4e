# ex13_using_API.py

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving:', url)
    uh = urllib.request.urlopen(url)    # uh → handle put the data down
    data = uh.read().decode()           # decode from UTF-8 → string
    print('Retrieved:', len(data), 'characters.')

    try:
        js = json.loads(data)           # parse data → dictionary
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']   # walking down the tree
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

