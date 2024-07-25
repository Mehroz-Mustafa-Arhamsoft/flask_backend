import os
from socketio import Server, WSGIApp
from dotenv import load_dotenv
from flask import Flask

from routes.scan_types import ScanTypes
from routes.socketio_handlers import SocketIOHandlers
from routes.flask_api import FlaskApi

load_dotenv()


class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.sio = Server(async_mode='threading')
        self.app.wsgi_app = WSGIApp(self.sio, self.app.wsgi_app)
        self.local_port = int(os.getenv('LOCAL_PORT', '8000'))

        self.register_blueprints()
        self.register_socketio_handlers()

    def register_blueprints(self):
        test_routes = FlaskApi()
        scan_types_routes = ScanTypes()

        self.app.register_blueprint(test_routes.blueprint, url_prefix='/')
        self.app.register_blueprint(scan_types_routes.blueprint, url_prefix='/')

    def register_socketio_handlers(self):
        socketio_handlers = SocketIOHandlers(self.sio)
        socketio_handlers.register_handlers()

    def run(self):
        self.app.run(debug=True, port=self.local_port)
