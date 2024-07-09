import os
from flask import Flask
from dotenv import load_dotenv
from routes.tests import tests_blueprint
from routes.scan_types import scan_types_blueprint

load_dotenv()
app = Flask(__name__)

local_port = int(os.getenv('LOCAL_PORT', '8000'))

app.register_blueprint(tests_blueprint, url_prefix='/')
app.register_blueprint(scan_types_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=local_port)
