from flask_restful import Resource

class HomePage(Resource):
    def get(self):
        return "Welcome on API home page"
