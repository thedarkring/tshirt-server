from time import sleep
import os


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
hotkey="Button"

def runProgram():
    print("Running program")
    os.system("echo 'Hello from the other side! We are working nowss!' > /tmp/hello")


try:
    while True:
        if GPIO.input(17) == GPIO.LOW:
            print("%s pressed, folding now..." % (hotkey))
            runProgram()
            sleep(1)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
