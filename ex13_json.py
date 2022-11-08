# ex13_json.py

import json

# ex1: dict in dict
data = '''{
    "name": "Chuck", 
    "phone": {
        "type": "intl", 
        "number": "+1 734 303 4456"
    }, 
    "email": {
        "hide": "yes"
    }

}'''

info = json.loads(data)
print('Name:', info["name"])            # Chuck
print('Hide:', info["email"]["hide"])   # yes
print()



# ex2: list of dict
input = '''[
    {"id": "001", 
    "x": "2", 
    "name": "Chuck"
    }, 
    {"id": "009", 
    "x": "7", 
    "name": "Ivca"
    }
]'''

info = json.loads(input)                # list
print(info, '\n')
print('User count:', len(info))         # User count: 2
for item in info:
    print('Name', item['name'])         # Name Chuck; Name Ivca (in next for cycle... )
    print('Id', item['id'])             # Id 001
    print('Attribute', item['x'])       # Attribute 2
