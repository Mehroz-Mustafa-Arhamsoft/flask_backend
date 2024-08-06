import subprocess

from utils.logger import append_to_logs


def zap_manager(log_file):
    append_to_logs("<--- ZAP INSTALLATION --->", console=True)

    # Install zap
    append_to_logs("(1) Checking if zap is installed", console=True)
    if is_zap_installed() == False:
        append_to_logs("(2) Installing zap", console=True)
        install_zap(log_file)
    else:
        append_to_logs("(2) zap is already installed", console=True)


def is_zap_installed():
    check_command = "dpkg -l | grep -w zap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_zap():
    check_command = "sudo apt install zap"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
