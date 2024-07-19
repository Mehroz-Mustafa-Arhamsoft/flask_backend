import os, socketio
from flask import Flask
from dotenv import load_dotenv
from routes.tests import tests_blueprint
from routes.scan_types import scan_types_blueprint
from routes.socketio_handlers import register_socketio_handlers

load_dotenv()
app = Flask(__name__)
sio = socketio.Server(async_mode='threading')
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

local_port = int(os.getenv('LOCAL_PORT', '8000'))

app.register_blueprint(tests_blueprint, url_prefix='/')
app.register_blueprint(scan_types_blueprint, url_prefix='/')

register_socketio_handlers(sio)

if __name__ == '__main__':
    app.run(debug=True, port=local_port)
    #socketio.run(app, port=local_port)
    #app.run(debug=True, port=local_port) 
