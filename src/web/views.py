from flask import render_template, Blueprint
from flask_restplus import Resource, Api, reqparse

from web.utils.db_extractor import get_total_delay
from web.utils.geo_decoder import GeoEncoder
from web.utils.accident_parser import AccidentParser

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
index_blueprint = Blueprint('api_views', __name__, template_folder='templates')
api = Api(api_blueprint)


@index_blueprint.route('/')
def index():
    return render_template('index.html')


@api.route('/ping')
class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}


# @api.route('/populate')
class Populate(Resource):
    def get(self):
        pupulator = AccidentParser('utils/ret.csv')  # not docker way
        pupulator.create_accident_table()
        pupulator.create_list_of_database_entries()
        pupulator.populate_database()
        return {'resopnse': 'population in progress'}


@api.route('/test_geo_encoder')
class TestGeoEncoder(Resource):
    def get(self):
        geo_encoder = GeoEncoder()
        test_response = geo_encoder.get_geo_coordinates("Centrum, Warszawa", 'street', radius=3000)
        return {'response': test_response}


@api.route('/test_db_connection')
class TestDbConnection(Resource):
    def get(self):
        test_result = get_total_delay(52.233407, 21.116504, 10, "2017-09-01")
        return {'result': test_result}


@api.route('/get_data')
class GetData(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fromDate', type=str, required=True)
        parser.add_argument('toDate', type=str, required=True)
        parser.add_argument('radius', type=int, required=True)
        args = parser.parse_args()

        print(args['radius'])
        data = get_total_delay(52.233407, 21.116504, 10, "2017-09-01")
        # NER + DB MAGIC
        # data = 'sampleData'
        return {'data': data}
