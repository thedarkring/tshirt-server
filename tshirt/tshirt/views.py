from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from time import sleep
from django.http import JsonResponse
import os
os.environ["FOLDING"] = "False"

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
 
pinNumbers=[2,3,4,27,22]
R1=2
R2=3
R3=4
R4=27
R5=22
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
        if (action) == 'heartbeat':
            folding = os.environ["FOLDING"]
            if folding == "True":
                folding = True
            else:
                folding = False
            context["folding"] = folding
        else:
            os.environ["FOLDING"] = "True"
            text_file = open("/tmp/action", "w")
            n = text_file.write(action)
            text_file.close()
            print(action)
            if action == "youth":
                GPIO.output(R1, 0)
                sleep(.2)
                GPIO.output(R3, 1)
                sleep(.4)
                GPIO.output(R3, 0)
                sleep(.4)
                GPIO.output(R4, 1)
                sleep(.4)
                GPIO.output(R4, 0)
                sleep(.4)
                GPIO.output(R5, 1)
                sleep(.4)
                GPIO.output(R5, 0)
                sleep(.4)
                GPIO.output(R1, 1)

            elif action == "fast":
                GPIO.output(R1, 0)
                sleep(.2)
                GPIO.output(R2, 1)
                sleep(.4)
                GPIO.output(R2, 0)
                sleep(.4)
                GPIO.output(R3, 1)
                sleep(.4)
                GPIO.output(R3, 0)
                sleep(.4)
                GPIO.output(R4, 1)
                sleep(.4)
                GPIO.output(R4, 0)
                sleep(.4)
                GPIO.output(R5, 1)
                sleep(.4)
                GPIO.output(R5, 0)
                sleep(.4)
                GPIO.output(R1, 1)

            elif action == "bulk":
                GPIO.output(R1, 0)
                sleep(.2)
                GPIO.output(R2, 1)
                sleep(.8)
                GPIO.output(R2, 0)
                sleep(.8)
                GPIO.output(R3, 1)
                sleep(.8)
                GPIO.output(R3, 0)
                sleep(.8)
                GPIO.output(R4, 1)
                sleep(.8)
                GPIO.output(R4, 0)
                sleep(.8)
                GPIO.output(R3, 1)
                sleep(.8)
                GPIO.output(R3, 0)
                sleep(.8)
                GPIO.output(R5, 1)
                sleep(.8)
                GPIO.output(R5, 0)
                sleep(.8)
                GPIO.output(R1, 1)


            elif action == "long":
                GPIO.output(R1, 0)
                sleep(.2)
                GPIO.output(R2, 1)
                sleep(.4)
                GPIO.output(R2, 0)
                sleep(.4)
                GPIO.output(R3, 1)
                sleep(.4)
                GPIO.output(R3, 0)
                sleep(.4)
                GPIO.output(R4, 1)
                sleep(.4)
                GPIO.output(R4, 0)
                sleep(.4)
                GPIO.output(R3, 1)
                sleep(.4)
                GPIO.output(R3, 0)
                sleep(.4)
                GPIO.output(R5, 1)
                sleep(.4)
                GPIO.output(R5, 0)
                sleep(.4)
                GPIO.output(R1, 1)

        return JsonResponse(context)