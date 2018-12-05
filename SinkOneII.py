import Adafruit_BBIO.GPIO as GPIO
import time

# from help on the googlegroups section of bbb.io!

class BrushedDC(object):
     def __init__(self, p1):
         self.p1 = p1
         #self.p2 = p2
         GPIO.setup(self.p1, GPIO.OUT)
         #GPIO.setup(self.p2, GPIO.OUT)
         self.stop()
     def stop(self):
         GPIO.output(self.p1, GPIO.LOW)
         #GPIO.output(self.p2, GPIO.LOW)
     def forward(self):
         self.stop()     #safety to avoid shock of reversals
         GPIO.output(self.p1, GPIO.HIGH)
         #GPIO.output(self.p2, GPIO.LOW)
     def reverse(self):
         self.stop()
         GPIO.output(self.p1, GPIO.LOW)
         #GPIO.output(self.p2, GPIO.HIGH)

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


myCar = Car(leftMotor=BrushedDC(p1="P9_42"))
             #rightMotor=BrushedDC(p1="P9_12", p2="P9_15"))

myCar.forward(10)
myCar.leftPivot(3)
myCar.forward(5)
myCar.rightTurnReverse(3)
myCar.reverse(10)
myCar.stop(10)
myCar.rightPivot(30)
myCar.forward(5)
myCar.rightTurnForward(15)
myCar.stop()

GPIO.cleanup()

