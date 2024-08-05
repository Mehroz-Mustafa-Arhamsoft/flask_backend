import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor
from shared_resources import test_queue, test_queue_lock
from utils.command_mapper import map_scan_type_to_command

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def map_scan_type_to_command(scan_type, target_ip, port_range):
    commands = {
        'sql': f'sqlmap -u {target_ip}',
        'http': f'wpscan --url {target_ip}',
        'vuln': f'zap-cli quick-scan --start {target_ip}',
        'portScan': f'nmap -p {port_range} {target_ip}'
    }
    return commands.get(scan_type.lower(), None)


def execute_test(test_id, scan_type, target_ip, port_range):
    try:
        command = map_scan_type_to_command(scan_type, target_ip, port_range)
        if not command:
            logging.error(f"Invalid scan type: {scan_type}")
            return

        logging.info(f"Starting {scan_type} scan for test_id: {test_id} with command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        with test_queue_lock:
            if test_id in test_queue:
                test_queue[test_id]['status'] = 'completed'
                test_queue[test_id]['result'] = result.stdout
                logging.info(f"Test {test_id} completed with {scan_type} scan.")
            else:
                logging.warning(f"Test {test_id} not found in test_queue.")
    except Exception as e:
        logging.error(f"Error in execute_test for test_id: {test_id}: {e}")


class Consumer:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.tasks = []

    def start_test(self, test_id, scan_type, target_ip, port_range):
        with test_queue_lock:
            test_queue[test_id] = {'status': 'in_progress', 'scan_type': scan_type}
        future = self.executor.submit(execute_test, test_id, scan_type, target_ip, port_range)
        self.tasks.append(future)

    def shutdown(self):
        logging.info("Shutting down consumer, waiting for all tasks to complete.")
        self.executor.shutdown(wait=True)
        logging.info("All tasks have completed.")


# Create a single instance of the Consumer and ensure it is shut down properly
consumer = Consumer(max_workers=5)

if __name__ == '__main__':
    consumer.start_test('test1', 'portScan', 'example.com', '1-1000')
    consumer.start_test('test2', 'vuln', 'example.com', '')
    consumer.start_test('test3', 'http', 'example.com', '')
    consumer.shutdown()
