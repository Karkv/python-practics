#PYTHON HAS A BUILD_IN PACKAGE CALLED JSON ,WHICH CAN BE USED TO WORK WITH JSON DATa.

import json

x='{"name":"Karan","age":23,"city":"India"}'
print(type(y))
y=json.loads(x)
print(type(y))
print(y["name"])
y=json.dumps(y)
print(type(y))