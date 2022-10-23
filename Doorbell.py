import time
import RPi.GPIO as GPIO
import subprocess

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN)

while True :
    etat = GPIO.input(BUTTON_PIN)

    if (etat == 0) :
        subprocess.Popen(["sudo", "service", "motion", "start"])
        time.sleep(60)
        subprocess.Popen(["killall", "motion"])
        time.sleep(3)
    time.sleep(0.3)
