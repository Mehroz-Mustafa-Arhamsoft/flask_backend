import subprocess
from .logger import append_to_logs
import os

def pip_manager(log_file, venv_path):
    append_to_logs("<--- PIP & VENV MANAGER --->", console=True)

    # Install venv
    append_to_logs("(1) Checking if python3-venv is installed", console=True)
    if is_python3_venv_installed() == False:
        append_to_logs("(2) Installing python3-venv", console=True)
        install_python3_venv(log_file)
    else:
        append_to_logs("(2) python3-venv is already installed", console=True)

    # Create venv
    append_to_logs(f"(3) Checking if python3-venv is available in {venv_path}", console=True)
    if is_venv_created(venv_path) == False:
        append_to_logs(f"(4) Creating python3-venv at {venv_path}", console=True)
        create_venv(venv_path, log_file)
    else:
        append_to_logs("(4) venv is already created", console=True)

    # Install pip
    append_to_logs("(5) Checking if pip is installed", console=True)
    if is_pip_installed() == False:
        append_to_logs("(6) Installing pip", console=True)
        install_pip(log_file)
    else:
        append_to_logs("(6) pip is already installed", console=True)

    # pip3 install -r requirements.txt
    append_to_logs("(7) Installing requirement.txt dependencies using pip", console=True)
    activate_venv_pip_install_req(log_file, venv_path)

def is_python3_venv_installed():
    check_command = "dpkg -l | grep -w python3-venv"
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def install_python3_venv(log_file):
    install_command = "sudo apt-get install -y python3-venv"
    with open(log_file, "a") as f:
        subprocess.run(install_command, shell=True, stdout=f, stderr=subprocess.STDOUT)

def is_venv_created(path):
    pyvenv_cfg = os.path.join(path, 'pyvenv.cfg')
    return os.path.isfile(pyvenv_cfg)

def create_venv(path, log_file):
    venv_command = f"python3 -m venv {path}"
    with open(log_file, "a") as f:
        subprocess.run(venv_command, shell=True, stdout=f, stderr=subprocess.STDOUT)

def install_pip(log_file):
    install_command = "sudo apt-get install -y pip"
    with open(log_file, "a") as f:
        subprocess.run(install_command, shell=True, stdout=f, stderr=subprocess.STDOUT)

def is_pip_installed():
    check_command = "dpkg -l | grep -w python3-pip" 
    result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def activate_venv_pip_install_req(log_file, venv_path):
    init_script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_py_exec = os.path.join(venv_path, "bin", "python3")
    pip_command = f"{venv_py_exec} -m pip3 install -r {init_script_dir}/../requirements.txt"
    with open(log_file, "a") as f:
        subprocess.run(pip_command, shell=True, stdout=f, stderr=subprocess.STDOUT)


if __name__ == "__main__":
    log_file = "/var/log/cybertester/cybertest.log"
    venv_path = "/home/poyo/Desktop/CyberTester/.venv"
    pip_manager(log_file, venv_path)