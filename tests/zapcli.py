import subprocess

def run_zapcli(target):
    try:
        cmd = ['zap-cli', 'quick-scan', '--self-contained', '-r', target]
        output = subprocess.run(cmd, capture_output=True, text=True)
        return {'output': output.stdout}
    except Exception as e:
        return {'error': str(e)}
