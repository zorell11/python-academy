from flask import Flask, jsonify, request, make_response

# Vytvoření aplikace
app = Flask(__name__)

# Provizorní databáze
customers = [
             {
              "email" : "jan.novak@email.cz",
              "username" : "johny",
              "name" : "Jan Novák",
              "newsletter_status" : True,
              "trips" : [
                            {
                             "destination" : "Oslo, Norway",
                             "price" : 150.00
                            },
                            {
                             "destination" : "Bangkok, Thailand",
                             "price" : 965.00
                            }
                          ]
             },
             {
              "email" : "ivan.opletal@gmail.com",
              "username" : "ivan123",
              "name" : "Ivan Opletal",
              "newsletter_status" : False,
              "trips" : []
             }
        ]
# Vrácení všech zákazníků
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify({'customers': customers}), 200

# Vrácení konkrétního zákazníka
@app.route('/customer/<string:username>', methods=['GET'])
def get_customer(username):
    for customer in customers:
        if customer['username'] == username:
            return jsonify(customer), 200
    return jsonify({'message': 'username not found'}), 404

# Vytvoření nového zákazníka
@app.route('/customer', methods=['POST'])
def create_customer():
    request_data = request.get_json()
    new_customer = {
        "email": request_data['email'],
        "username": request_data['username'],
        "name": request_data['name'],
        "newsletter_status": request_data['newsletter_status'],
        "trips": []
    }
    for customer in customers:
        if customer['username'] == new_customer['username']:
            return jsonify({'error': 'username already exist'}), 409
    customers.append(new_customer)
    return jsonify(new_customer), 201

# Vrácení všech zájezdů pod zákaníkem
@app.route('/customer/<string:username>/trips', methods=['GET'])
def get_trips_in_customer(username):
    for customer in customers:
        if customer['username'] == username:
            return jsonify({'trips': customer['trips']})
    return jsonify({'message': 'username not found'}), 404

# Vytvoření zájezdu pod zákazníkem
@app.route('/customer/<string:username>/trips', methods=['POST'])
def create_trip_in_customer(username):
    for customer in customers:
        if customer['username'] == username:
            request_data = request.get_json()
            new_trip = {
                "destination": request_data['destination'],
                "price": request_data['price']
            }
            customer['trips'].append(new_trip)
            return new_trip, 201
    return jsonify({'message': 'username not found'}), 404

# Spuštění serveru
app.run(port=3333, debug=True)
