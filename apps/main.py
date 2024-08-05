from tests.nmap import run_nmap
from tests.nikto import run_nikto
from tests.sqlmap import run_sqlmap
from tests.wpscan import run_wpscan
from tests.zapcli import run_zapcli

TOOLS = {
    'nmap': run_nmap,
    'nikto': run_nikto,
    'wpscan': run_wpscan,
    'sqlmap': run_sqlmap,
    'zapcli': run_zapcli
}

def run_tool(tool, target):
    if tool in TOOLS:
        return TOOLS[tool](target)
    else:
        return {'error': 'Tool not supported'}
