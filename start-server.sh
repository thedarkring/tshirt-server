#!/usr/bin/bash
# version 2
PATH=/home/pi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
cd /home/pi/tshirt/tshirt-server/
git pull
. /home/pi/tshirt/bin/activate
mv /home/pi/tshirt/tshirt-server/start-server.sh /home/pi/start-server.sh
python /home/pi/tshirt/tshirt-server/tshirt/manage.py runserver 0.0.0.0:8080
