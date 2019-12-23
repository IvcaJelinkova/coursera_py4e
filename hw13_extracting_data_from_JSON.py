# hw13_extracting_data_from_JSON.py

# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data, compute the sum
# of the numbers in the file and enter the sum below.

# ex of data:
# data = '''
# {
#     "note": "This file contains",
#     "comments": [
#         {
#             "name": "Romina",
#             "count": 97
#         },
#         {
#             "name": "Laurie",
#             "count": 97
#         },
#         {
#             "name":  "Ivča",
#             "count": 88
#         },
#        ...
#     ]
# }'''

import urllib.request, urllib.parse, urllib.error
import json

user_url = input('Enter url: ')
if len(user_url) < 1:
    user_url = 'http://py4e-data.dr-chuck.net/comments_42.json'  # Sum = 2553

print('Retrieving:', user_url)

handle_url = urllib.request.urlopen(user_url)
data = handle_url.read().decode()
print('Retrieved:', len(data), 'characters.')

js = json.loads(data)
sum = 0
for value in js['comments']:
    #print('value:', value)      # dict
    #print(value['count'])
    num = value['count']
    sum += num
    #print('actual sum:', sum)
print('sum =', sum)




