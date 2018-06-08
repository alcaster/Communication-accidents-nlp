from flask import render_template, Blueprint, current_app
from flask_restplus import Resource, Api

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
