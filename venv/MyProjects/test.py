import requests

parameters =  {
    "lat":50.0614,
    "lng": 19.9366,
}
URL = 'https://api.sunrise-sunset.org/json'

URL2 = 'https://dummyjson.com/products/1'
x = requests.get(URL, params= parameters)
data = x.json()
print(data['results']['sunrise'])
print(data['results']['sunset'])



