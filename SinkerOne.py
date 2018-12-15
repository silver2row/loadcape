import Adafruit_BBIO.GPIO as GPIO
import time

# from help on the googlegroups section of bbb.io, i.e. circa 2016...2017.

m1 = "P9_42"
m2 = "P9_41"

class LeftMotor(object):

     def __init__(self, m1):
         self.m1 = m1
         GPIO.setup(self.m1, GPIO.OUT)
         self.stop()

     def stop(self):
         GPIO.output(self.m1, GPIO.LOW)

     def forward(self):
         GPIO.output(self.m1, GPIO.HIGH)

     def reverse(self):
         GPIO.output(self.m1, GPIO.HIGH)

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
        self.stop()

    def stop(self, go=5):
        self.LeftMotor.stop()
        time.sleep(1)

    def forward(self, go=5):
        self.LeftMotor.forward()
        time.sleep(1)

    def reverse(self, go=5):
        self.LeftMotor.reverse()
        time.sleep(1)

    def leftTurnForward(self, go=5):
        self.leftMotor.stop()
        time.sleep(1)

    def rightTurnForward(self, go=5):
        self.LeftMotor.forward()
        time.sleep(1)

    def leftTurnReverse(self, go=5):
        self.LeftMotor.stop()
        time.sleep(1)

    def rightTurnReverse(self, go=5):
        self.LeftMotor.reverse()
        time.sleep(1)

    def leftPivot(self, go=5):
        self.LeftMotor.reverse()
        time.sleep(1)

    def rightPivot(self, go=5):
        self.LeftMotor.forward()
        time.sleep(1)

class RightWheel(object):

    def __init__(self, RightMotor):
        self.RightMotor = RightMotor
        self.stop()

    def stop(self, go=5):
        self.RightMotor.stop()
        time.sleep(1)

    def forward(self, go=5):
        self.RightMotor.forward()
        time.sleep(1)

    def reverse(self, go=5):
        self.RightMotor.reverse()
        time.sleep(1)

    def leftTurnForward(self, go=5):
        self.RightMotor.forward()
        time.sleep(1)

    def rightTurnForward(self, go=5):
        self.RightMotor.stop()
        time.sleep(1)

    def leftTurnReverse(self, go=5):
        self.RightMotor.reverse()
        time.sleep(1)

    def rightTurnReverse(self, go=5):
        self.RightMotor.stop()
        time.sleep(1)

    def leftPivot(self, go=5):
        self.RightMotor.forward()
        time.sleep(1)

    def rightPivot(self, go=5):
        self.RightMotor.reverse()
        time.sleep(1)

Left = LeftWheel(LeftMotor=LeftMotor(m1="P9_42"))

Right = RightWheel(RightMotor=RightMotor(m2="P9_41"))

Left.forward(5)
Right.forward(5)

Left.stop(5)
Right.stop(5)

Left.rightPivot(5)
Right.rightPivot(5)

Left.stop()
Right.stop()

GPIO.cleanup()


