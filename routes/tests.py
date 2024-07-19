from flask import Blueprint, request, jsonify
import uuid
import time
from models import Test
from common import tests, tests_lock
from services.test_worker import start_test_worker

tests_blueprint = Blueprint('tests', __name__)

@tests_blueprint.route('/trigger-test', methods=['POST'])
def trigger_test():
    data = request.get_json()
    test_id = str(uuid.uuid4())
    timestamp_started = int(time.time())
    expected_ending = timestamp_started + 3600
    
    test = Test(
        test_id=data["test_id"],
        timestamp_started=timestamp_started,
        expected_ending=expected_ending,
        test_type=data["test_type"],
        target_ip=data["target_ip"],
        port_range=data["port_range"],
        status="in_progress"
    )
    
    with tests_lock:
        tests[test_id] = test.to_dict()
    
    duration = 60                            
    start_test_worker(test_id, duration)    # ToDo - Simulating Work - Remove After implementing real work needed
    
    return jsonify(test.to_dict())

@tests_blueprint.route('/get-scan-status', methods=['POST'])
def get_scan_status():
    data = request.get_json()
    test_id = data["testId"]
    
    with tests_lock:
        if test_id in tests:
            return jsonify(tests[test_id])
        else:
            return jsonify({"error": "Test ID not found"}), 404

@tests_blueprint.route('/get-result', methods=['POST'])
def get_result():
    data = request.get_json()
    test_id = data["testId"]
    format_required = data["format_required"]
    
    with tests_lock:
        if test_id in tests:
            test = tests[test_id]
            if test['status'] != 'completed':
                return jsonify({"error": "Test is not yet completed"}), 400
            
            result = {
                "testId": test_id,
                "timestampStarted": test["timestampStarted"],
                "expectedEnding": test["expectedEnding"],
                "type": test["type"],
                "target_ip": test["target_ip"],
                "port_range": test["port_range"],
                "result": "This is a placeholder result"
            }
            
            if format_required == "json":
                return jsonify(result)
            else:
                return jsonify({"error": "Unsupported format requested"}), 400
        else:
            return jsonify({"error": "Test ID not found"}), 404
