import json
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def calculateDeliveryFee(cartValue, deliveryDistance, numberOfItems):
    deliveryFee = 0
    if (cartValue >= 200):
        return 0
    if (cartValue < 10):
        deliveryFee = 10 - cartValue
    if (4 < numberOfItems < 13):
        deliveryFee += numberOfItems * 0.5
    elif (numberOfItems >= 13):
        deliveryFee += (numberOfItems * 0.5) + 1.2
    if (deliveryDistance > 1000):
        deliveryFee += math.ceil((deliveryDistance - 1000) / 500)
    if (deliveryFee > 15):
        return 15
    return deliveryFee

@app.route('/calculateDeliveryFee', methods=['POST'])
def CalculatorAPI():
    try:
        data = request.get_json()
        
        cartValue = data.get('cartValue', 0)
        deliveryDistance = data.get('deliveryDistance', 0)
        numberOfItems = data.get('numberOfItems', 0)

        deliveryFee = calculateDeliveryFee(cartValue, deliveryDistance, numberOfItems)

        response = {'deliveryFee': deliveryFee}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run()