from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

from AVSummarizer.config import Config, app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    CORS(app, resources={r"/*": {"origins": "*"}})

    from AVSummarizer.avtosummary.routes import avtosummary
    app.register_blueprint(avtosummary)

    return app
