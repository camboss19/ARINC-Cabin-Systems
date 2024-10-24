#Relay test for the PSU
# Runs through all of the relays connected to the audio hat

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

light1=12
light2=13
light3=16
FAcall=5
noSmoke=6
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(FAcall, GPIO.OUT)
GPIO.setup(noSmoke, GPIO.OUT)

def test(x):
    print("Testing: ",x)
    for y in range(3):
        GPIO.output(x,1)
        time.sleep(1)

def main():
    print("In gpioControl Main")
    test(light1)
    test(light2)
    test(light3)
    test(FAcall)
    test(noSmoke)

main()
GPIO.cleanup()