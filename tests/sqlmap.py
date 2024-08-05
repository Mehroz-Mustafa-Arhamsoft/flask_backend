import subprocess

def run_sqlmap(target, port=""):
    try:
        cmd = ['sqlmap', '-u', target, port]
        output = subprocess.run(cmd, capture_output=True, text=True)
        return {'output': output.stdout}
    except Exception as e:
        return {'error': str(e)}
