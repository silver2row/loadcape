#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

Master_Pin1 =  "P9_42"

Master_Pin2 =  "P9_41"

if __name__=="__main__":

    GPIO.setup(Master_Pin1, GPIO.OUT)
    GPIO.setup(Master_Pin2, GPIO.OUT)

    while True:

        GPIO.output(Master_Pin1, GPIO.LOW)
        GPIO.output(Master_Pin2, GPIO.LOW)


        GPIO.output(Master_Pin1, GPIO.HIGH)
        GPIO.output(Master_Pin2, GPIO.HIGH)
        time.sleep(10)

        GPIO.output(Master_Pin1, GPIO.LOW)
        GPIO.output(Master_Pin2, GPIO.LOW)
        time.sleep(5)

        GPIO.output(Master_Pin1, GPIO.HIGH)
        GPIO.output(Master_Pin2, GPIO.LOW)
        time.sleep(8)

        GPIO.output(Master_Pin1, GPIO.LOW)
        GPIO.output(Master_Pin2, GPIO.LOW)

        GPIO.cleanup()
