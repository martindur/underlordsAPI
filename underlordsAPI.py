import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


safe_types = [
    'units',
    'abilities',
    'synergies',
    'items'
]


class Index(Resource):
    def get(self):
        return {'Underlords API': '1.0'}


class DataList(Resource):
    def get(self, data_list):
        if data_list not in safe_types:
            return {'Error': 'Unsupported data'}
        with open(f'game_data/{data_list}.json', 'r') as file:
            return json.load(file)


class DataUnit(Resource):
    def get(self, data_list, data_unit):
        if data_list not in safe_types:
            return {'Error': 'Unsupported data'}
        with open(f'game_data/{data_list}.json', 'r') as file:
            data = json.load(file)
            try:
                return data[data_unit]
            except KeyError:
                return {'Error': 'Unsupported data'}


api.add_resource(Index, '/')
api.add_resource(DataList, '/<string:data_list>')
api.add_resource(DataUnit, '/<string:data_list>/<string:data_unit>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)