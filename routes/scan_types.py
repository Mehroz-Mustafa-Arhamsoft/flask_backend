from flask import Blueprint, jsonify


class ScanTypes:
    def __init__(self):
        self.blueprint = Blueprint('scan_types', __name__)
        self.setup_routes()

    def setup_routes(self):
        @self.blueprint.route('/scan-types', methods=['GET'])
        def get_scan_types():
            return jsonify({
                "types": ["portScan", "vuln", "http", "sql"]
            })
