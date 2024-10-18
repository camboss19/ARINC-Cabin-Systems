import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin23=23
GPIO.setup(pin1, GPIO.OUT)


def main():
    print("In gpioControl Main")

    # Control 
    # Turn on:
    # GPIO.output(pin23,1)
    # Turn off:
    # GPIO.output(pin23,0)

    GPIO.cleanup()
