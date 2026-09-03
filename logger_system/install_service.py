import shutil
import subprocess
import os
import sys
from pathlib import Path

def install_mail_cron(user):
    print("Stating mail service installations..")
    cron_job = (
        f"0 17 * * * "  #Once every day at 5 pm
        f"/home/{user}/.local/bin/send-monthly-mail "
        f">> /home/{user}/.logs/mail-cron.log 2>&1"
    )

    result = subprocess.run(
        ["sudo", "-u", user, "crontab", "-l"],
        capture_output=True,
        text=True
    )

    existing = result.stdout if result.returncode == 0 else ""

    if cron_job in existing:
        print("Mail cron already installed.")
        return

    new_crontab = existing.rstrip() + "\n" + cron_job + "\n"

    subprocess.run(
        ["sudo", "-u", user, "crontab", "-"],
        input=new_crontab,
        text=True,
        check=True
    )

    print("Mail cron installed.")

def install_service(user):

    import logger_system
    package_dir = os.path.dirname(logger_system.__file__)
    robot_id = os.environ["ROBOT_ID"] # If the script runs with sudo, USER = root and SUDO_USER = duet.
                                      # If run with no sudo, SUDO_USER = none and USER = duet
    
    #============== Delete old logs folder =====================
    old_logs_dir = f"/home/{user}/.logs"
    os.makedirs(f"/home/{user}/temp_logs", exist_ok=True)

    try:
        shutil.copy(f"/home/{user}/.logs/logs.txt",f"/home/{user}/temp_logs") 
    except FileNotFoundError:
        print("No logs.txt file to copy. Continue..")
    try:
        shutil.copy(f"/home/{user}/.logs/latest-stats.pdf",f"/home/{user}/temp_logs") 
    except FileNotFoundError:
        print("No latest-stats.pdf file to copy. Continue..")
    try:
        shutil.copy(f"/home/{user}/.logs/last_sent.txt",f"/home/{user}/temp_logs") 
    except FileNotFoundError:
        print("No last_sent.txt file to copy. Continue..")
    try:
        shutil.copytree(f"/home/{user}/.logs/old_logs",f"/home/{user}/temp_logs/old_logs")
    except Exception as e:
        print("No old_logs folder was found")

    if os.path.exists(old_logs_dir):
        shutil.rmtree(old_logs_dir)  

    os.makedirs(f"/home/{user}/.logs", exist_ok=True)
    # move files to .logs
    try:
        shutil.move(f"/home/{user}/temp_logs/logs.txt",f"/home/{user}/.logs/")
    except FileNotFoundError:
        print("No previous Logs were found!")
    try:
        shutil.move(f"/home/{user}/temp_logs/latest-stats.pdf",f"/home/{user}/.logs/")
    except FileNotFoundError:
        pass
    try:
        shutil.move(f"/home/{user}/temp_logs/last_sent.txt",f"/home/{user}/.logs/")
    except:
        pass
    try:
        shutil.copytree(f"/home/{user}/temp_logs/old_logs",f"/home/{user}/.logs/old_logs")
    except Exception as e:
        os.makedirs(f"/home/{user}/.logs/old_logs", exist_ok=True)
        print("Creating old_logs folder")
        print(f"ERROR copying old_logs: {e}")
        raise        
    
    if os.path.exists(f"/home/{user}/temp_logs"): #remove temo folder
        shutil.rmtree(f"/home/{user}/temp_logs")  
    #============================================================

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

def add_credentials():
    credentials_folder=Path("~/.config/logger_credentials").expanduser()
    credentials_folder.mkdir(parents=True, exist_ok=True)

    credentials_file=credentials_folder / "credentials.txt"
    CLIENT_SECRET = input("Please enter the client secret: ")
    REFRESH_TOKEN = input("Please enter the refresh token: ")

    with open(credentials_file, "w") as f:
        f.write(f"CLIENT_SECRET {CLIENT_SECRET} \n")
        f.write(f"REFRESH_TOKEN {REFRESH_TOKEN} \n")

def main():
    user = os.getenv("SUDO_USER") or os.getenv("USER")
    install_service(user)
    install_mail_cron(user)
    add_credentials(user)
    print("robot-logger package installed successfully")


if __name__ == "__main__":
    main()