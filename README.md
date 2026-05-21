# New system:
Run the following in the same order:</br> 
1. If you are installing the logger for the first time, run: **pip install --upgrade pip** 
2. pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/Abdelrahman97omar/logger.git
3. ~/.local/bin/logger-install
4. The logger.py, creatreport.py and install_service.py (package installer) will be installed into /home/USER/.local/lib/python3.10/site-packages/logger_system  
4. The logs file (logs.txt) and the report pdf (latest-stats.pdf) will be in /home/USER/.logs
# Old way to install logger
1. Send **"logger.zip"** and **"installScript.sh"** to robot's home  
2. Extract logger.zip
3. open terminal and run the following two comands: </br>
    a. chmod 777 installScript.sh </br>
    b. ./installScript.sh
4. go in logger folder, open loger.py and replace the time zone in the following line: tz = pytz.timezone('Africa/Cairo'). You will find all time zone options in the loger.py file
5. restart the robot and in home, open .logs folder and make sure logs.txt file is present
