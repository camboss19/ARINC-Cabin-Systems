#PSUcontrol

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

light1=12
light2=13
light3=16
FAcall=5
seatbelt=6
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(FAcall, GPIO.OUT)
GPIO.setup(seatbelt, GPIO.OUT)

def on(x):
    print("Turn on: ",x)
    GPIO.output(x,1)
def off(x):
    print("Turn off: ",x)
    GPIO.output(x,0)  

def lightOn():
    on(light1)
    on(light2)
    on(light3)
def lightOff():
    off(light1)
    off(light2)
    off(light3)

def faOn():
    on(FAcall)
def faOff():
    off(FAcall)

def seatOn():
    on(seatbelt)
def seatOff():
    off(seatbelt)