import requests
import json
# city=input("Enter City\n")
city="Delhi"
# appid="852aabe2b9fa456630d55d0f7035f26a"
appid="4a1f8a61b74546825af1e0be106e797b"
url="https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(city,appid)
response = requests.get(url)
data = response.json()
print(data)