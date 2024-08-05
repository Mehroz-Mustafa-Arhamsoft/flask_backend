import requests
import json

SERVER_URL = 'http://127.0.0.1:5000'

def run_scan(tool, target):
    payload = {
        'tool': tool,
        'target': target
    }
    response = requests.post(f'{SERVER_URL}/run_test', json=payload)
    if response.status_code == 200:
        result_file = response.json().get('result_file')
        if result_file:
            print(f'Scan initiated. Result file: {result_file}')
            return result_file
        else:
            print('Error in initiating scan:', response.json().get('error'))
    else:
        print('Failed to contact server:', response.status_code)

def get_result(filename):
    response = requests.get(f'{SERVER_URL}/get_result/{filename}')
    if response.status_code == 200:
        print('Scan Results:')
        print(response.json().get('result'))
    else:
        print('Failed to retrieve result:', response.status_code)

if __name__ == "__main__":
    tool = input("Enter the tool (nmap/nikto/wpscan/sqlmap/zapcli): ")
    target = input("Enter the target URL/IP: ")
    
    result_file = run_scan(tool, target)
    if result_file:
        input("Press Enter to retrieve results...")
        get_result(result_file)
