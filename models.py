class Test:
    def __init__(self, test_id, timestamp_started, expected_ending, test_type, target_ip, port_range, status):
        self.testId = test_id
        self.timestampStarted = timestamp_started
        self.expectedEnding = expected_ending
        self.type = test_type
        self.target_ip = target_ip
        self.port_range = port_range
        self.status = status

    def to_dict(self):
        return {
            "testId": self.testId,
            "timestampStarted": self.timestampStarted,
            "expectedEnding": self.expectedEnding,
            "type": self.type,
            "target_ip": self.target_ip,
            "port_range": self.port_range,
            "status": self.status
        }
