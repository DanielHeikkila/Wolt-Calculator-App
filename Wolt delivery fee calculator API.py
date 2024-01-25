import json
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

#Main calculation function
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

#This here takes the json sent by the frontends as shown in the "import requests.py" file
@app.route('/calculateDeliveryFee', methods=['POST'])
def CalculatorAPI():
    try:
        data = request.get_json()
        
        #Makes Python values out of the json
        cartValue = data.get('cartValue', 0)
        deliveryDistance = data.get('deliveryDistance', 0)
        numberOfItems = data.get('numberOfItems', 0)
        time_str = data.get('time', '')
        timeOfOrder = datetime.fromisoformat(time_str)
        logging.info(f'{numberOfItems}, {deliveryDistance} , {cartValue}, {timeOfOrder}')

        #Calls the calculator function
        deliveryFee = calculateDeliveryFee(cartValue, deliveryDistance, numberOfItems)

        #Sends result back as json
        response = {'deliveryFee': deliveryFee}
        return jsonify(response), 200
    #In case of error sends back the error message
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run()
