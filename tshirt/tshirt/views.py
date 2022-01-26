from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from time import sleep
from django.http import JsonResponse
import os
import pickle
import json
# fold_counts = { 'fast-count': 0, 'youth-count': 0, 'long-count': 0, 'bulk-count': 0}

##

os.environ["FOLDING"] = "False"
# with open('fold-counts.json', 'wb') as fp:
#     pickle.dump(my_dict, fp)
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
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
hotkey="Button"
 
pinNumbers=[4,5,7,17,22]
R1=4
R2=5
R3=7
R4=17
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

try:
    with open('fold-counts.json', 'rb') as fp:
        fold_counts = pickle.load(fp)
except:
     fold_counts = { 'fast-count': 0, 'youth-count': 0, 'long-count': 0, 'bulk-count': 0}

@method_decorator(csrf_exempt, name='dispatch')
class DashboardView(View):

    def __init__(self):
        print("init dashboard")

    def get(self, request):
        context = dict()
        return render(request, 'index.html', context)

    def post(self, request):

        folding = os.environ["FOLDING"]
        if folding == "True":
            folding = True
        else:
            folding = False
        context = dict()
        
        action = request.POST.get("action")
        if (action) == 'reset':
            fold_counts["youth-count"] = 0
            fold_counts["fast-count"] = 0
            fold_counts["bulk-count"] = 0
            fold_counts["long-count"] = 0
        if (action) == 'heartbeat':
            context["folding"] = folding

        elif folding == False:
            os.environ["FOLDING"] = "True"
            text_file = open("/tmp/action", "w")
            n = text_file.write(action)
            text_file.close()
            print(action)
            # if action == "reset":

            if action == "youth":
                fold_counts["youth-count"] = fold_counts["youth-count"] + 1
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
                fold_counts["fast-count"] = fold_counts["fast-count"] + 1
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
                fold_counts["bulk-count"] = fold_counts["bulk-count"] + 1
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
                fold_counts["long-count"] = fold_counts["long-count"] + 1
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
            os.environ["FOLDING"] = "False"
            with open('fold-counts.json', 'wb') as fp:
                pickle.dump(fold_counts, fp)
        context["fold-counts"] = fold_counts
        return JsonResponse(context)
