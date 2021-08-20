#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = {'pin_R':11, 'pin_G':13, 'pin_B':18}

GPIO.setmode(GPIO.BOARD)
for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)


def returnColor(temp, humi):
    if temp < 22:
        if humi < 40: # color white
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.LOW)
            GPIO.output(pins['pin_B'], GPIO.LOW)
        elif 40 <= humi <=70:   # color light blue
            GPIO.output(pins['pin_R'], GPIO.HIGH)
            GPIO.output(pins['pin_G'], GPIO.LOW)
            GPIO.output(pins['pin_B'], GPIO.LOW)
        else:   # color blue
            GPIO.output(pins['pin_R'], GPIO.HIGH)
            GPIO.output(pins['pin_G'], GPIO.HIGH)
            GPIO.output(pins['pin_B'], GPIO.LOW)
    elif 22 <= temp <= 28:
        if humi < 40: # color purple
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.HIGH)
            GPIO.output(pins['pin_B'], GPIO.LOW)
        elif 40 <= humi <=70: # color green
            GPIO.output(pins['pin_R'], GPIO.HIGH)
            GPIO.output(pins['pin_G'], GPIO.LOW)
            GPIO.output(pins['pin_B'], GPIO.HIGH)
        else:   # color purple
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.HIGH)
            GPIO.output(pins['pin_B'], GPIO.LOW)
    else:
        if humi < 40: # color yellow
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.LOW)
            GPIO.output(pins['pin_B'], GPIO.HIGH)
        elif 40 <= humi <=70:   # color red
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.HIGH)
            GPIO.output(pins['pin_B'], GPIO.HIGH)
        else:   # color red
            GPIO.output(pins['pin_R'], GPIO.LOW)
            GPIO.output(pins['pin_G'], GPIO.HIGH)
            GPIO.output(pins['pin_B'], GPIO.HIGH)

def turn_off_led():
        for i in pins:
                GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
        GPIO.cleanup()

        