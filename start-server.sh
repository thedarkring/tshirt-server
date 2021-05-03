#!/usr/bin/bash
# version 2
PATH=/home/pi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
cd /home/pi/tshirt/tshirt-server/
find .git/objects/ -size 0 -delete
git reset --hard HEAD
git pull
. /home/pi/tshirt/bin/activate
# pip install -r requirements.txt
cp /home/pi/tshirt/tshirt-server/start-server.sh /home/pi/start-server.sh
chmod +x /home/pi/tshirt/tshirt-server/listen_button.py
nohup python3 /home/pi/tshirt/tshirt-server/listen_button.py &
python3 /home/pi/tshirt/tshirt-server/tshirt/manage.py runserver 0.0.0.0:8080
