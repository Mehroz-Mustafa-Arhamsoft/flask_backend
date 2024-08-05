import os
from flask import current_app as app, request, jsonify
from .main import run_tool

@app.route('/run_test', methods=['POST'])
def run_test():
    data = request.get_json()
    tool = data.get('tool')
    target = data.get('target')
    result = run_tool(tool, target)
    
    result_file = f"output/results_{tool}_{target.replace('.', '_')}.txt"
    with open(result_file, 'w') as file:
        file.write(result['output'])
    
    return jsonify({'result_file': result_file})

@app.route('/get_result/<filename>', methods=['GET'])
def get_result(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return jsonify({'result': file.read()})
    else:
        return jsonify({'error': 'File not found'})
