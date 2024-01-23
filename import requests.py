import requests

url = 'http://127.0.0.1:5000/calculateDeliveryFee'
data = {
    'cartValue': 120,
    'deliveryDistance': 3400,
    'numberOfItems': 15
}

response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print(f'Delivery Fee: {result["deliveryFee"]}')
else:
    print(f'Error: {response.text}')