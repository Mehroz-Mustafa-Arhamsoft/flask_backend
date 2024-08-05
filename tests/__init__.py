import subprocess

# Dictionary to map tool names to functions
TOOLS = {}

# Decorator to register a tool
def register_tool(name):
    def decorator(func):
        TOOLS[name] = func
        return func
    return decorator

# Register the tools dynamically
from .nmap import run_nmap
from .nikto import run_nikto
from .wpscan import run_wpscan
from .sqlmap import run_sqlmap
from .zapcli import run_zapcli

register_tool('nmap')(run_nmap)
register_tool('nikto')(run_nikto)
register_tool('wpscan')(run_wpscan)
register_tool('sqlmap')(run_sqlmap)
register_tool('zapcli')(run_zapcli)

def run_tool(tool, target):
    try:
        func = TOOLS.get(tool)
        if func:
            return func(target)
        else:
            return {'error': 'Tool not supported'}
    except Exception as e:
        return {'error': str(e)}
