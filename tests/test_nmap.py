import logging
from logging.handlers import RotatingFileHandler
import os
import subprocess
import asyncio
from utils.file_handler import save_json_output, convert_xml_to_json
from utils.logger import append_to_logs


log_file = "/var/log/cybertester/cybertest.log"


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.debug("message")

class NmapScanner:
    def __init__(self):
        self.scan_commands = {
            'host_discovery': ['-sn', '-PE', '-PP', '-PM', '-PS80,443', '-PA80,443'],
            'tcp_udp_comprehensive': ['-sS', '-sU', '-p', '1-65535', '-sV'],
            'aggressive': ['-A'],
            'all_ports_os': ['-sS', '-sU', '-p-', '-O'],
            'firewall_evasion': ['-sS', '-f', '--mtu', '16', '-D', 'RND:10,ME'],
            'sctp_comprehensive': ['-sY', '-sZ', '-p', '1-65535'],
            'ip_protocol': ['-sO'],
            'timing_optimization': ['-sS', '-T4', '-p', '1-65535', '--min-rate', '500', '--max-rate', '1000'],
            'custom_tcp': ['--scanflags', 'SYNFIN', '-p', '1-65535'],
            'traceroute_ping': ['--traceroute', '-sn'],
            'detailed_scan': ['-A', '-sS', '-T4', '--top-ports', '1000', '-v', '--reason', '--version-all']
        }

    async def run_scan(self, scan_type: str, target_host: str, output_file: str) -> None:
        if scan_type not in self.scan_commands:
            raise ValueError(f"Invalid scan type: {scan_type}")

        options = self.scan_commands[scan_type]
        command = ['sudo', 'nmap', '-v', '-oX', '-'] + options + [target_host]
        logging.debug(f"Starting NMap {scan_type.replace('_', ' ').title()} on {target_host}")

        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            logging.debug("Nmap scan completed successfully")
            xml_output = stdout.decode()
            json_output = convert_xml_to_json(xml_output)
            save_json_output(json_output, output_file)
        else:
            logging.error(f"Nmap scan failed with error: {stderr.decode()}")
            raise Exception(f"Nmap scan failed with error: {stderr.decode()}")
