from flask_restful import Resource, reqparse
from auth import api_key_required
from models.customers import CustomerModel

class Customers(Resource):
    @api_key_required
    def get(self):
        customers = []
        for customer in CustomerModel.query.all():
            customers.append(customer.json())
        return customers, 200


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('newsletter_status', type=bool, required=True)

    #@api_key_required
    def post(self, username):
        if CustomerModel.find_by_username(self, username):
            return {'error': 'username already exist'}, 409
        data = self.parser.parse_args()
        new_customer = CustomerModel(username, data['email'], data['name'], data['newsletter_status'])
        new_customer.create_customer()
        return new_customer.json(), 201

    def get(self, username):
        customer = CustomerModel.find_by_username(self, username)
        if customer:
                return customer.json(), 200
        return {'message': 'username not found'}, 404



    def put(self, username):
        data = self.parser.parse_args()
        user_data = CustomerModel(username, data["email"], data["name"], data["newsletter_status"])
        customer = CustomerModel.find_by_username(self, username)
        if customer:
            customer.email = data['email']
            customer.create_customer()
            return customer.json(), 200
        else:
            user_data.create_customer()
            return user_data.json(), 201


    def delete(self, username):
        customer = CustomerModel.find_by_username(self, username)
        if customer:
            customer.delete_from_database()
            return {'message': 'user is deleted'}, 200
        else:
            return {'message': 'username not found'}, 404
