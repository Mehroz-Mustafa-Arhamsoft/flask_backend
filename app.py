from flask import Flask
from routes.tests import tests_blueprint
from routes.scan_types import scan_types_blueprint

app = Flask(__name__)

app.register_blueprint(tests_blueprint, url_prefix='/')
app.register_blueprint(scan_types_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
