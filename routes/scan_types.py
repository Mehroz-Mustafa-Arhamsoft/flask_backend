from flask import Blueprint, jsonify

scan_types_blueprint = Blueprint('scan_types', __name__)

@scan_types_blueprint.route('/scan-types', methods=['GET'])
def scan_types():
    return jsonify({
        "types": ["portScan", "vuln", "http", "sql"]
    })
