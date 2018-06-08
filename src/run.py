from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from web.views import index_blueprint, api_blueprint
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(index_blueprint)
app.register_blueprint(api_blueprint)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
