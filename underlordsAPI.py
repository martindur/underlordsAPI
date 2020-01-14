import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return {'Underlords API': '1.0'}


class Units(Resource):
    def get(self):
        with open('../game_data/units.json' 'r') as f:
            return f


class Unit(Resource):
    def get(self, unit):
        pass