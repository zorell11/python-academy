from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

customers = [
             {
              "email" : "jan.novak@exammple.cz",
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

class Customers(Resource):
    def get(self):
        return {'customers': customers}, 200

class Customer(Resource):
    def get(self, username):
        for customer in customers:
            if customer['username'] == username:
                return customer, 200
        return {'message': 'username not found'}, 404

    def post(self, username):
        request_data = request.get_json()
        new_customer = {
            "email": request_data['email'],
            "username": username,
            "name": request_data['name'],
            "newsletter_status": request_data['newsletter_status'],
            "trips": []
        }
        for customer in customers:
            if customer['username'] == new_customer['username']:
                return {'error': 'username already exist'}, 409
        customers.append(new_customer)
        return new_customer, 201

    def put(self, username):
        request_data = request.get_json()
        updated_customer = {
            "email": request_data['email'],
            "username": username,
            "name": request_data['name'],
            "newsletter_status": request_data['newsletter_status'],
            "trips": []
        }
        for customer in customers:
            if customer['username'] == updated_customer['username']:
                customer.update(request_data)
                return updated_customer, 201
        customers.append(updated_customer)
        return updated_customer, 201

    def delete(self, username):
        for customer in customers:
            if username == customer['username']:
                customers.remove(customer)
                return {'message': 'customer was successfully removed'}, 200
        return {'message': 'username not found'}, 404

class Trips(Resource):
    def get(self, username):
        for customer in customers:
            if customer['username'] == username:
                return {'trips': customer['trips']}, 200
        return {'message': 'username not found'}, 404

    def post(self, username):
        for customer in customers:
            if customer['username'] == username:
                request_data = request.get_json()
                new_trip = {
                    "destination": request_data['destination'],
                    "price": request_data['price']
                }
                customer['trips'].append(new_trip)
                return new_trip, 201
        return {'message': 'username not found'}, 404

api.add_resource(Customers, '/customers')
api.add_resource(Customer, '/customer/<string:username>')
api.add_resource(Trips, '/customer/<string:username>/trips')

# Spuštění serveru
app.run(port=3333, debug=True)
