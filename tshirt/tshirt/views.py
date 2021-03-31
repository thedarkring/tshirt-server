from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from time import sleep
import sys
import fake_rpi


try:
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
except:
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
hotkey="Button"
 
pinNumbers=[2,3,4,27,22]
for pinNumber in pinNumbers:
    GPIO.setup(pinNumber, GPIO.OUT)
    
def runProgram():
    print("Running program")
    for pinNumber in pinNumbers:
        GPIO.output(pinNumber, 1)
        sleep(.5)

@method_decorator(csrf_exempt, name='dispatch')
class DashboardView(View):

    def __init__(self):
        print("init dashboard")

    def get(self, request):
        context = dict()
        return render(request, 'index.html', context)

    def post(self, request):
        context = dict()
        runProgram()
        return render(request, 'index.html', context)