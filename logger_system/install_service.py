import shutil
import subprocess
import os
import sys
from pathlib import Path

def install_service():

    import logger_system
    package_dir = os.path.dirname(logger_system.__file__)
    # If the script runs with sudo USER = root and SUDO_USER = duet. If run with no sudo, SUDO_USER = none and USER = duet
    user = os.getenv("SUDO_USER") or os.getenv("USER")
    robot_id = os.environ["ROBOT_ID"]

    # Remove old logs file
    try:
        print("Copying old logs to safe place")
        shutil.copy(f"/home/{user}/.logs/logs.txt",f"/home/{user}/") #Copy old logs file to home
    except:
        print("Could'nt copy old logs")
    old_logs_dir = f"/home/{user}/.logs"
    if os.path.exists(old_logs_dir):
        shutil.rmtree(old_logs_dir)  

    os.makedirs(f"/home/{user}/.logs", exist_ok=True)
    #move files to .logs
    try:
        shutil.move(f"/home/{user}/logs.txt",f"/home/{user}/.logs/")
    except FileNotFoundError:
        print("No previous Logs were found!")

    shutil.copy(os.path.join(package_dir, "run-log.sh"),f"/home/{user}/.logs")
    shutil.copy(os.path.join(package_dir, "loger.py"), f"/home/{user}/.logs")
    shutil.copy(os.path.join(package_dir, "creatreport.py"), f"/home/{user}/.logs")
    os.chmod(f"/home/{user}/.logs", 0o777)

    #install Service
    subprocess.run(["sudo","systemctl", "stop", "logger"])
    service_file_content = Path(os.path.join(package_dir, "logger.service"))
    service_src = os.path.join(package_dir, "logger.service")

    # Add the robot user and id to the service file
    content = service_file_content.read_text()
    content = content.replace("__USER__", user)
    content = content.replace("__ROBOTID__", robot_id)
    service_file_content.write_text(content)

    subprocess.run(["sudo", "cp", f"{service_src}", "/etc/systemd/system/logger.service"])      
    subprocess.run(["sudo", "systemctl", "daemon-reload"])         
    subprocess.run(["sudo", "systemctl", "enable", "logger"])      
    subprocess.run(["sudo", "systemctl", "start", "logger"])       

if __name__ == "__main__":
    install_service()