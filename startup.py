"""
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
"""
import os
import subprocess
import tools
# from apps import create_app
from tools import nmap, wpscan, sqlmap, nikto, zap
from utils.config_loader import Configuration
from utils.pip_manager import pip_manager

log_dir_path = "/var/log/cybertester/"
reports_path = "/etc/cybertester/"
venv_path = "/opt/cybertester/.venv"
log_file = "/var/log/cybertester/cybertest.log"
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "cybertester.config")
configurations = Configuration(config_path)

tools_list = configurations.get_tools()

pip_manager(log_file, venv_path)

if "nmap" in tools_list:
    nmap.nmap_manager(log_file)
if "wpscan" in tools_list:
    wpscan.wpscan_manager(log_file)
if "nikto" in tools_list:
    nikto.nikto_manager(log_file)
if "sqlmap" in tools_list:
    sqlmap.sqlmap_manager(log_file)
# if "zap" in tools_list:
#     zap.zap_manager(log_file)
