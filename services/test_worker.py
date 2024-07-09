import threading
import time
from config import tests, tests_lock

def test_worker(test_id, duration):
    time.sleep(duration)  # Simulate a long-running test
    with tests_lock:
        if test_id in tests:
            tests[test_id]['status'] = 'completed'

def start_test_worker(test_id, duration):
    threading.Thread(target=test_worker, args=(test_id, duration)).start()
