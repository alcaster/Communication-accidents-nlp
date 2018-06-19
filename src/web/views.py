from flask import render_template, Blueprint
from flask_restplus import Resource, Api, reqparse

from web.utils.geo_decoder import GeoEncoder
from web.utils.db_extractor import get_total_delay, get_points_in_range

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
        radius = args.radius
        data = get_points_in_range(args.fromDate, args.toDate)
        # data = [[str(i[0]), i[6], i[7]] for i in data]
        # print(data)
        # print(type(data))
        # circles = []
        # for row in data:
        #     print(row)
        #     date = row[0]
        #     lon = row[1]
        #     lat = row[2]
        #     result = get_total_delay(lon, lat, radius, date)
        #     print("hello" + str(result))
        #     circles.append([lon, lat, result])

        circles=[[row[6],row[7],get_total_delay(row[6],row[7],radius, str(row[0]))] for row in data]

        return {'data':circles}
        #return {'data':data}

        # data = get_total_delay(52.233407, 21.116504, 10, "2017-09-01")
        # # NER + DB MAGIC
        # #data = 'sampleData'
        # return {'data': data}
