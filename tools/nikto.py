import subprocess

from utils.logger import append_to_logs


def nikto_manager(log_file):
    append_to_logs("<--- NIKTO INSTALLATION --->", console=True)

    # Install nikto
    append_to_logs("(1) Checking if nikto is installed", console=True)
    if is_nikto_installed() == False:
        append_to_logs("(2) Installing nikto", console=True)
        install_nikto(log_file)
    else:
        append_to_logs("(2) nikto is already installed", console=True)


def is_nikto_installed():
    check_command = "dpkg -l | grep -w nikto"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_nikto():
    check_command = "sudo apt install nikto"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
