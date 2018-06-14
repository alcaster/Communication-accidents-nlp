from flask import render_template, Blueprint
from flask_restplus import Resource, Api

from web.utils.geo_decoder import GeoEncoder
from web.utils.db_extractor import DbExtractor

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

@index_blueprint.route('/ula')
def ula_test():
    return render_template('file.html')


@api.route('/test_geo_encoder')
class TestGeoEncoder(Resource):
    def get(self):
        geo_encoder = GeoEncoder()
        test_response = geo_encoder.get_geo_coordinates("Centrum, Warszawa", 'street', radius=3000)
        return {'response': test_response}

@api.route('/test_db_connection')
class TestDbConnection(Resource):
    def get(self):
        db_extractor = DbExtractor()
        test_result = DbExtractor.get_total_delay(52.233407,21.116504,10, "2017-09-01")
        return {'result':test_result}

@api.route('/get_data')
class GetData(Resource):
    def get(self, time_start, time_end, radius):
        # Karol

        #
        return {'ping': 'pong'}
