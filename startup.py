import asyncio
import logging
import os
import subprocess
from tests.test_nmap import NmapScanner
import tools
# from apps import create_app
from tools import nmap, wpscan, sqlmap, nikto, zap
from utils.config_loader import Configuration
from utils.pip_manager import pip_manager

# log_dir_path = "/var/log/cybertester/"
# reports_path = "/etc/cybertester/"
# venv_path = "/opt/cybertester/.venv"
# log_file = "/var/log/cybertester/cybertest.log"
# current_dir = os.path.dirname(os.path.abspath(__file__))
# config_path = os.path.join(current_dir, "cybertester.config")
# configurations = Configuration(config_path)

# tools_list = configurations.get_tools()

# pip_manager(log_file, venv_path)

# if "nmap" in tools_list:
#     nmap.nmap_manager(log_file)
# if "wpscan" in tools_list:
#     wpscan.wpscan_manager(log_file)
# if "nikto" in tools_list:
#     nikto.nikto_manager(log_file)
# if "sqlmap" in tools_list:
#     sqlmap.sqlmap_manager(log_file)
# if "zap" in tools_list:
#     zap.zap_manager(log_file)


async def main():
    nmap_scanner = NmapScanner()
    target_ip = "192.168.9.79"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_dir, "output/nmap_scan.json")

    try:
        await nmap_scanner.run_scan("host_discovery", target_ip, output_file)
        logging.debug(f"NMap JSON output saved to {output_file}")
    except Exception as e:
        logging.error(f"An error occurred during Nmap scan: {e}")

if __name__ == "__main__":
    asyncio.run(main())