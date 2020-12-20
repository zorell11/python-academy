from flask_restful import Resource, reqparse
from auth import api_key_required
from models.trips import TripModel

class Trips(Resource):
    #@api_key_required
    def get(self):
        trips = []
        for trips in TripModel.query.all():
            trips.append(trips.json())
        return customers, 200


class Trip(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('destination', type=str, required=True)
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('customer_username', type=str, required=True)

#@api_key_required
    def get(self, trip_id):
        trip = TripModel.find_by_id(trip_id)
        if trip:
            return trip.json(), 200
        return {'message': 'trip not found'}, 404

    def post(self, trip_id):
        if TripModel.find_by_trip_id(self, trip_id):
            return {'error': 'trip already exist'}, 409
        data = self.parser.parse_args()
        new_trip = TripModel(trip_id, **data)
        new_trip.create_trip()
        return new_trip.json(), 201
