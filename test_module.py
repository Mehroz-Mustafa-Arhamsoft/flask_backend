class TestModule:
    def __init__(self, test_id, timestamp_started, expected_ending, test_type, target_ip, port_range, status):
        self.test_id = test_id
        self.timestamp_started = timestamp_started
        self.expected_ending = expected_ending
        self.test_type = test_type
        self.target_ip = target_ip
        self.port_range = port_range
        self.status = status

    def to_dict(self):
        return {
            "test_id": self.test_id,
            "timestamp_started": self.timestamp_started,
            "expected_ending": self.expected_ending,
            "test_type": self.test_type,
            "target_ip": self.target_ip,
            "port_range": self.port_range,
            "status": self.status
        }
