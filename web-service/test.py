import requests

house = {
    "squareMeters": 10750,

}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=house)
print(response.json())
