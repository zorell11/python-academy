from flask import Flask, request
from flask_restful import Resource, Api, reqparse

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
api = Api(app)

class HomePage(Resource):
    def get(self):
        return "Hello Flask-RESTful!"


class Customers(Resource):
    def get(self):
        return {'customers' : customers}, 200


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('newsletter_status', type=bool, required=True)
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

    def delete(self, username):
        for customer in customers:
            if username == customer['username']:
                customers.remove(customer)
                return {'message' : 'customer was successfully removed'}, 200
        return {'message' : 'User do not exist'}, 404

    def put(self, username):
        request_data = request.get_json()
        user_data = {
        "email" : request_data["email"],
        "name" : request_data["name"],
        "newsletter_status" : request_data["newsletter_status"]
        }
        for customer in customers:
            if username == customer['username']:
                customer.update(user_data)
                return user_data, 201
        customer.append(user_data)
        return user_data, 201

class Trips(Resource):
    def get(self, username):
        for customer in customers:
            if customer['username'] == username:
                return {'trips': customer['trips']}, 200
        return {'message': 'username not found'}, 404

    def post(self, username):
            request_data = request.get_json()
            new_trip = {
            "destination" : request_data["destination"],
            "price" : request_data["price"]
            }
            for customer in customers:
                if username == customer['username']:
                    customer['trips'].append(new_trip)
                    return {'trips' : customer['trips']}, 201
            return {'message' : 'User do not exist'}, 404



api.add_resource(HomePage, '/')
api.add_resource(Customers, '/customers')
api.add_resource(Customer, '/customer/<string:username>')
api.add_resource(Trips, '/customer/<string:username>/trips')
app.run(port=3333, debug=True)
