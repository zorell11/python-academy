from flask import Flask, jsonify, request

customers = [
             {
              "email" : "jan.novak@example.cz",
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
              "email" : "ivan.opletal@example.com",
              "username" : "ivan123",
              "name" : "Ivan Opletal",
              "newsletter_status" : False,
              "trips" : []
             }
        ]


app = Flask(__name__)

################  GET
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my API page", 200


@app.route('/customers', methods=['GET'])
def all_customer():
    return jsonify(customers), 200

@app.route('/customer/<string:username>', methods=['GET'])
def get_customer(username):
    for customer in customers:
        if username == customer['username']:
            return jsonify(customer), 200
    return "User do not exist", 404


@app.route('/customer/<string:username>/trips', methods=['GET'])
def get_trip(username):
    for customer in customers:
        if username == customer['username']:
            return jsonify({'trips' : customer['trips']}), 200
    return "User do not exist", 404

################ POST
@app.route('/customer/<string:username>/trips', methods=['POST'])
def add_trip(username):
    request_data = request.get_json()
    new_trip = {
    "destination" : request_data["destination"],
    "price" : request_data["price"]
    }
    for customer in customers:
        if username == customer['username']:
            customer['trips'].append(new_trip)
            return jsonify({'user' : customer}), 201
    return "User do not exist", 404


@app.route('/customer', methods=['POST'])
def add_customer(username):
    request_data = request.get_json()
    new_customer = {
    "username" : username,
    "email" : request_data["email"],
    "username" : request_data["username"],
    "name" : request_data["name"],
    "newsletter_status" : request_data["newsletter_status"],
    "trips" : []
    }
    for customer in customers:
        if new_customer['username'] == customer['username']:
            return "User is already exist", 409
    customers.append(new_customer)
    return jsonify({'user' : new_customer}), 201


############### PUT
@app.route('/customer/<string:username>', methods=['PUT'])
def change_user(username):
    request_data = request.get_json()
    user_data = {
    "email" : request_data["email"],
    "name" : request_data["name"],
    "newsletter_status" : request_data["newsletter_status"]
    }
    for customer in customers:
        if username == customer['username']:
            customer.update(user_data)
            return jsonify({ 'user' : customer}), 201
        return "User do not exist", 404

########## DELETE

@app.route('/customer/<string:username>', methods=['DELETE'])
def delete_user(username):
    for customer in customers:
        if username == customer['username']:
            customers.remove(customer)
            return "User deleted", 200
    return "User do not exist", 404


app.run(port=3333, debug=True)
