import requests

#Here is how you access the API with the json

#This is the url for the request
url = 'http://127.0.0.1:5000/calculateDeliveryFee'

#This is the json
data = {
    'cartValue': 120,
    'deliveryDistance': 3400,
    'numberOfItems': 15
}

#Here is the request and where you would handle the response
response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print(f'Delivery fee: {result["deliveryFee"]}')
else:
    print(f'Error: {response.text}')