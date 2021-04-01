from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from time import sleep




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
hotkey="Button"
 

for pinNumber in pinNumbers:
    GPIO.setup(pinNumber, GPIO.OUT)
    
def runProgram(pinNumbers):
    print("Running program")
    for pinNumber in pinNumbers:
        GPIO.output(pinNumber, 1)
        sleep(.5)
    sleep(.5)
    for pinNumber in pinNumbers:
        GPIO.output(pinNumber, 0)
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
        
        action = request.POST.get("action")
        text_file = open("/tmp/action", "w")
        n = text_file.write(action)
        text_file.close()
        print(action)
        if action == "youth":
            pinNumbers=[2,3]
        elif action == "fast":
            pinNumbers=[4]
        elif action == "bulk":
            pinNumbers=[2,3,4,27,22]
        elif action == "long":
            pinNumbers=[2,3,4]
        runProgram(pinNumbers)
        return render(request, 'index.html', context)