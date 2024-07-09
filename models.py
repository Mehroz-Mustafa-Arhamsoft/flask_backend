class Test:
    def __init__(self, test_id, timestamp_started, expected_ending, test_type, target_ip, port_range, status):
        self.testId = test_id
        self.timestampStarted = timestamp_started
        self.expectedEnding = expected_ending
        self.type = test_type
        self.targetIp = target_ip
        self.portRange = port_range
        self.status = status

    def to_dict(self):
        return {
            "testId": self.testId,
            "timestampStarted": self.timestampStarted,
            "expectedEnding": self.expectedEnding,
            "type": self.type,
            "targetIp": self.targetIp,
            "portRange": self.portRange,
            "status": self.status
        }
