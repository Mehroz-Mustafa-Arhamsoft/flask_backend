# utils/command_mapper.py

def map_scan_type_to_command(scan_type, target_ip, port_range):
    commands = {
        'sql': f'sqlmap -u {target_ip}',
        'http': f'wpscan --url {target_ip}',
        'vuln': f'zap-cli quick-scan --start {target_ip}',
        'portScan': f'nmap -p {port_range} {target_ip}'
    }
    return commands.get(scan_type.lower(), None)
