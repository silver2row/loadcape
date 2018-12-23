#!/usr/bin/python3

from SinkerOneII import *
import time

m1 = "P9_42"

while True:

    if m1 == 1:
        if forward == 8:
            forward = time.time() + 8

    else:
        if time.time() > forward:
            print("Um...")

left.forward(8)
time.sleep(5)

left.reverse(8)
time.sleep(5)

left.stop()
