import subprocess

from utils.logger import append_to_logs


def sqlmap_manager(log_file):
    append_to_logs("<--- SQLMAP INSTALLATION --->", console=True)

    # Install sqlmap
    append_to_logs("(1) Checking if sqlmap is installed", console=True)
    if is_sqlmap_installed() == False:
        append_to_logs("(2) Installing sqlmap", console=True)
        install_sqlmap(log_file)
    else:
        append_to_logs("(2) sqlmap is already installed", console=True)


def is_sqlmap_installed():
    check_command = "dpkg -l | grep -w sqlmap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_sqlmap():
    check_command = "sudo apt install sqlmap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
