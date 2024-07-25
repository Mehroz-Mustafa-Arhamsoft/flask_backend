import time
import uuid
import atexit
from flask import Blueprint, request, jsonify
from services.consumer import consumer, Consumer
from shared_resources import test_queue, test_queue_lock
from test_module import TestModule


class FlaskApi:
    def __init__(self):
        self.blueprint = Blueprint('tests', __name__)
        self.setup_routes()

    def setup_routes(self):
        @self.blueprint.route('/trigger-test', methods=['POST'])
        def trigger_test():
            data = request.get_json()
            scan_type = data.get("test_type")
            valid_scan_types = {"portScan", "vuln", "http", "sql"}

            if scan_type not in valid_scan_types:
                return jsonify({"error": "Invalid scan type"}), 400

            test_id = str(uuid.uuid4())
            timestamp_started = int(time.time())
            expected_ending = timestamp_started + 3600

            test = TestModule(
                test_id=test_id,
                timestamp_started=timestamp_started,
                expected_ending=expected_ending,
                test_type=scan_type,
                target_ip=data["target_ip"],
                port_range=data["port_range"],
                status="in_progress"
            )

            with test_queue_lock:
                test_queue[test_id] = test.to_dict()

            duration = 60
            consumer.start_test(test_id, scan_type, data["target_ip"], data["port_range"])

            return jsonify(test.to_dict())

        @self.blueprint.route('/get-scan-status', methods=['POST'])
        def get_scan_status():
            data = request.get_json()
            test_id = data["test_id"]

            with test_queue_lock:
                if test_id in test_queue:
                    return jsonify(test_queue[test_id])
                else:
                    return jsonify({"error": "Test ID not found"}), 404

        @self.blueprint.route('/get-result', methods=['POST'])
        def get_result():
            data = request.get_json()
            test_id = data["test_id"]
            format_required = data["format_required"]

            with test_queue_lock:
                if test_id in test_queue:
                    test = test_queue[test_id]
                    if test['status'] != 'completed':
                        return jsonify({"error": "Test is not yet completed"}), 400

                    result = {
                        "test_id": test_id,
                        "timestamp_started": test["timestamp_started"],
                        "expected_ending": test["expected_ending"],
                        "test_type": test["test_type"],
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


# Create a single instance of the Consumer and ensure it is shut down properly
worker = Consumer(max_workers=5)
atexit.register(worker.shutdown)
