'''
    if you have a python object, you can convert it into a JSON string hy using the json.dumps() method.

'''

import json

#a python object dict:

x={
    "name":"Karan"
    ,"age": 23
    ,"city":"India"
}

y=json.dumps(x)
print(y)