import subprocess

def run_nikto(target):
    try:
        cmd = ['nikto', '-h', target]
        output = subprocess.run(cmd, capture_output=True, text=True)
        return {'output': output.stdout}
    except Exception as e:
        return {'error': str(e)}
