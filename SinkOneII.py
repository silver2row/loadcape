import Adafruit_BBIO.GPIO as GPIO
import time

# from help on the googlegroups section of bbb.io!

class BrushedDC(object):

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
         GPIO.output(self.m1, GPIO.LOW)
         #GPIO.output(self.m2, GPIO.HIGH)

class BrushedDCII(object):

    def __init__(self, m2):
        self.m2 = m2
        GPIO.setup(self.m2, GPIO.OUT)
        self.stop()

    def stop(self):
        GPIO.output(self.m2, GPIO.LOW)

    def forward(self):
        GPIO.output(self.m2, GPIO.LOW)

    def reverse(self):
        GPIO.output(self.m2, GPIO.HIGH)

class Car(object):
    def __init__(self, leftMotor):
        self.leftMotor = leftMotor
        #self.rightMotor = rightMotor
        self.stop()
    def stop(self, wait=0):
        self.leftMotor.stop()
        #self.rightMotor.stop()
        time.sleep(wait)
    def forward(self, wait=0):
        self.leftMotor.forward()
        #self.rightMotor.forward()
        time.sleep(wait)
    def reverse(self, wait=0):
        self.leftMotor.reverse()
        #self.rightMotor.reverse()
        time.sleep(wait)
    def leftTurnForward(self, wait=0):
        self.leftMotor.stop()
        #self.rightMotor.forward()
        time.sleep(wait)
    def rightTurnForward(self, wait=0):
        self.leftMotor.forward()
        #self.rightMotor.stop()
        time.sleep(wait)
    def leftTurnReverse(self, wait=0):
        self.leftMotor.stop()
        #self.rightMotor.reverse()
        time.sleep(wait)
    def rightTurnReverse(self, wait=0):
        self.leftMotor.reverse()
        #self.rightMotor.stop()
        time.sleep(wait)
    def leftPivot(self, wait=0):
        self.leftMotor.reverse()
        #self.rightMotor.forward()
        time.sleep(wait)
    def rightPivot(self, wait=0):
        self.leftMotor.forward()
        #self.rightMotor.reverse()
        time.sleep(wait)

class CarII(object):

    def __init__(self, rightMotor):
        self.rightMotor = rightMotor
        self.stop()
    def stop(self, wait=0):
        self.rightMotor.stop()
        time.sleep(wait)
    def forward(self, wait=0):
        self.rightMotor.forward()
        time.sleep(wait)
    def reverse(self, wait=0):
        self.rightMotor.reverse()
        time.sleep(wait)
    def leftTurnForward(self, wait=0):
        self.rightMotor.forward()
        time.sleep(wait)
    def rightTurnForward(self, wait=0):
        self.rightMotor.stop()
        time.sleep(wait)
    def leftTurnReverse(self, wait=0):
        self.rightMotor.reverse()
        time.sleep(wait)
    def rightTurnReverse(self, wait=0):
        self.rightMotor.stop()
        time.sleep(wait)
    def leftPivot(self, wait=0):
        self.rightMotor.forward()
        time.sleep(wait)
    def rightPivot(self, wait=0):
        self.rightMotor.reverse()
        time.sleep(wait)

myCar = Car(leftMotor=BrushedDC(m1="P9_42"))

myCarII = CarII(rightMotor=BrushedDCII(m2="P9_41"))

myCar.forward(5)
myCar.leftPivot(5)
myCar.forward(5)
myCar.rightTurnReverse(5)
myCar.reverse(5)
myCar.stop(2)
myCar.rightPivot(5)
myCar.forward(5)
myCar.rightTurnForward(5)
myCar.stop()

myCarII.forward(5)
myCarII.leftPivot(5)
myCarII.forward(5)
myCarII.rightTurnReverse(5)
myCarII.reverse(5)
myCarII.stop(2)
myCarII.rightPivot(5)
myCarII.forward(5)
myCarII.rightTurnForward(5)
myCarII.stop()

GPIO.cleanup()

