#!/usr/bin/python3

from SinkerOneII import *
import time

m1 = "P9_42"

while True:
    GPIO.output(m1, GPIO.HIGH)
    time.sleep(5)
    print("Moving on down the road!")

    GPIO.output(m1, GPIO.LOW)
    time.sleep(10)
    print("Stopping this boat!")
