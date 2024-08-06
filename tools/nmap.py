import subprocess

from utils.logger import append_to_logs


def nmap_manager(log_file):
    append_to_logs("<--- NMAP INSTALLATION --->", console=True)

    # Install nmap
    append_to_logs("(1) Checking if Nmap is installed", console=True)
    if is_nmap_installed() == False:
        append_to_logs("(2) Installing Nmap", console=True)
        install_nmap(log_file)
    else:
        append_to_logs("(2) Nmap is already installed", console=True)


def is_nmap_installed():
    check_command = "dpkg -l | grep -w nmap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_nmap():
    check_command = "sudo apt install nmap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
