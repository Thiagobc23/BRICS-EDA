from flask import Flask
from flask_restful import Api, Resource
import db_handler

app = Flask(__name__)
api = Api(app)

class Brics(Resource):
    def get(self):
        return db_handler.to_json('brics')

class Countries(Resource):
    def get(self):
        return db_handler.to_json('countries')

class Names(Resource):
    def get(self):
        return db_handler.to_json('names')

class Years(Resource):
    def get(self):
        return db_handler.to_json('years')

api.add_resource(Brics, "/brics")
api.add_resource(Countries, "/countries")
api.add_resource(Names, "/names")
api.add_resource(Years, "/years")

if __name__ == "__main__":
    app.run(debug=True)