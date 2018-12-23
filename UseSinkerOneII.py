#!/usr/bin/python3

from SinkerOneII import *
import time

m1 = "P9_42"

while True:

    if m1 == 1:
        if Left.forward == 8:
            Left.forward = 8
            time.sleep(2)

    else:
        if Left.forward == 9:
            Left.reverse = 8
            time.sleep(2)
            print("Um...")

left.stop()
