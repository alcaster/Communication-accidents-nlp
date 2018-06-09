from flask import render_template, Blueprint
from flask_restplus import Resource, Api

from web.utils.geo_decoder import GeoEncoder

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


@api.route('/test_geo_encoder')
class TestGeoEncoder(Resource):
    def get(self):
        geo_encoder = GeoEncoder()
        test_response = geo_encoder.get_geo_coordinates("Centrum, Warszawa", 'street', radius=3000)
        return {'response': test_response}
