from time import sleep
import os



try:
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
except:
    import fake_rpi
    import sys
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

import requests
url='http://127.0.0.1:8080'

def runProgram():
    post = {'fold': 'green'}
    x = requests.post(url, data = post)

try:
    while True:
        if GPIO.input(17) == GPIO.LOW:
            runProgram()
            sleep(1)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()

    
    
    
    
    
    
    




