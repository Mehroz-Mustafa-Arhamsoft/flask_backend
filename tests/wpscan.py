import subprocess

def run_wpscan(target):
    try:
        cmd = ['wpscan', '--url', target]
        output = subprocess.run(cmd, capture_output=True, text=True)
        return {'output': output.stdout}
    except Exception as e:
        return {'error': str(e)}
