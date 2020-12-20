from database import db

class TripModel(db.Model):
    __tablename__ = 'trip'

    trip_id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    customer_username = db.Column(db.ForeignKey('customers.username'))
    customer = db.relationship('CustomerModel')

    trips = db.relationship('TripModel')

    def __init__(self, trip_id, destination, price, customer_username):
        self.trip_id = trip_id
        self.destination = destination
        self.price = price
        self.customer_username = customer_username

    def find_by_trip_id(self, trip_id):
        return TripModel.query.filter_by(trip_id=trip_id).first()

    def json(self):
        return {
            'trip_id': self.trip_id,
            'destination': self.destination,
            'price': self.price,
            'customer_username': self.customer_username
            }

    def create_trip(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()
