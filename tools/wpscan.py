import subprocess

from utils.logger import append_to_logs


def wpscan_manager(log_file):
    append_to_logs("<--- WPSCAN INSTALLATION --->", console=True)

    # Install gem
    append_to_logs("(1) Checking if gem is installed", console=True)
    if is_gem_installed() == False:
        append_to_logs("(2) Installing gem", console=True)
        install_gem(log_file)
    else:
        append_to_logs("(2) gem is already installed", console=True)
    
    # Install wpscan
    append_to_logs("(1) Checking if wpscan is installed", console=True)
    if is_wpscan_installed() == False:
        append_to_logs("(2) Installing wpscan", console=True)
        install_wpscan(log_file)
    else:
        append_to_logs("(2) wpscan is already installed", console=True)


def is_gem_installed():
    check_command = "dpkg -l | grep -w gem"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_gem():
    check_command = "sudo apt install gem"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def is_wpscan_installed():
    check_command = "gem list | grep -w wpscan"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_wpscan():
    check_command = "sudo gem install wpscan"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
