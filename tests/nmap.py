import subprocess

def run_nmap(target, ports=""):
    try:
        cmd = ['nmap', target, ports]
        output = subprocess.run(cmd, capture_output=True, text=True)
        return {'output': output.stdout}
    except Exception as e:
        return {'error': str(e)}
