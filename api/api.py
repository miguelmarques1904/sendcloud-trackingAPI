from flask import Flask
from flask_restful import Api
from api.resources.emailTracking import EmailTracking


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    api = Api(app)
    api.add_resource(EmailTracking, '/email')

    return app