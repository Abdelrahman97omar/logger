sed -i "s/__USER__/$USER/g" /home/${USER}/logger/logger.service
sed -i "s/__ROBOTID__/$ROBOT_ID/g" /home/${USER}/logger/logger.service
echo 12345 | sudo -S cp /home/${USER}/logger/logger.service /etc/systemd/system
sudo systemctl enable logger.service
mkdir -p /home/${USER}/.logs/
cd /home/${USER}/logger
cp * /home/${USER}/.logs/
cd /home/${USER}/.logs/
pip install -r requirements.txt
