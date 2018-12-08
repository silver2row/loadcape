import Adafruit_BBIO.GPIO as GPIO
import time

# from help on the googlegroups section of bbb.io!

class LeftMotor(object):

     def __init__(self, m1):
         self.m1 = m1
         #self.m2 = m2
         GPIO.setup(self.m1, GPIO.OUT)
         #GPIO.setup(self.m2, GPIO.OUT)
         self.stop()

     def stop(self):
         GPIO.output(self.m1, GPIO.LOW)
         #GPIO.output(self.m2, GPIO.LOW)

     def forward(self):
         self.stop()     #safety to avoid shock of reversals
         GPIO.output(self.m1, GPIO.HIGH)
         #GPIO.output(self.m2, GPIO.LOW)

     def reverse(self):
         self.stop()
         GPIO.output(self.m1, GPIO.HIGH)
         #GPIO.output(self.m2, GPIO.HIGH)

class RightMotor(object):

    def __init__(self, m2):
        self.m2 = m2
        GPIO.setup(self.m2, GPIO.OUT)
        self.stop()

    def stop(self):
        GPIO.output(self.m2, GPIO.LOW)

    def forward(self):
        GPIO.output(self.m2, GPIO.HIGH)

    def reverse(self):
        GPIO.output(self.m2, GPIO.HIGH)

class LeftWheel(object):
    def __init__(self, LeftMotor):
        self.LeftMotor = LeftMotor
        #self.rightMotor = rightMotor
        self.stop()
    def stop(self, wait=0):
        self.LeftMotor.stop()
        #self.rightMotor.stop()
        time.sleep(wait)
    def forward(self, wait=0):
        self.LeftMotor.forward()
        #self.rightMotor.forward()
        time.sleep(wait)
    def reverse(self, wait=0):
        self.LeftMotor.reverse()
        #self.rightMotor.reverse()
        time.sleep(wait)
    def leftTurnForward(self, wait=0):
        self.leftMotor.stop()
        #self.rightMotor.forward()
        time.sleep(wait)
    def rightTurnForward(self, wait=0):
        self.LeftMotor.forward()
        #self.rightMotor.stop()
        time.sleep(wait)
    def leftTurnReverse(self, wait=0):
        self.LeftMotor.stop()
        #self.rightMotor.reverse()
        time.sleep(wait)
    def rightTurnReverse(self, wait=0):
        self.LeftMotor.reverse()
        #self.rightMotor.stop()
        time.sleep(wait)
    def leftPivot(self, wait=0):
        self.LeftMotor.reverse()
        #self.rightMotor.forward()
        time.sleep(wait)
    def rightPivot(self, wait=0):
        self.LeftMotor.forward()
        #self.rightMotor.reverse()
        time.sleep(wait)

class RightWheel(object):

    def __init__(self, RightMotor):
        self.RightMotor = RightMotor
        self.stop()
    def stop(self, wait=0):
        self.RightMotor.stop()
        time.sleep(wait)
    def forward(self, wait=0):
        self.RightMotor.forward()
        time.sleep(wait)
    def reverse(self, wait=0):
        self.RightMotor.reverse()
        time.sleep(wait)
    def leftTurnForward(self, wait=0):
        self.RightMotor.forward()
        time.sleep(wait)
    def rightTurnForward(self, wait=0):
        self.RightMotor.stop()
        time.sleep(wait)
    def leftTurnReverse(self, wait=0):
        self.RightMotor.reverse()
        time.sleep(wait)
    def rightTurnReverse(self, wait=0):
        self.RightMotor.stop()
        time.sleep(wait)
    def leftPivot(self, wait=0):
        self.RightMotor.forward()
        time.sleep(wait)
    def rightPivot(self, wait=0):
        self.RightMotor.reverse()
        time.sleep(wait)

Left = LeftWheel(LeftMotor=LeftMotor(m1="P9_42"))

Right = RightWheel(RightMotor=RightMotor(m2="P9_41"))

Left.forward(5)
Right.forward(5)

Left.stop(5)
Right.stop(5)

Left.reverse(5)
Right.reverse(5)

Left.stop()
Right.stop()

GPIO.cleanup()

