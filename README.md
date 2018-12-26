# loadcape

...

Hello...this is GHI's LoadCape w/ BeagleBoard.org. GHI manufactured it.

# Starter Software

...

I have listed some starter software for your LoadCape. It basically controls two DC motors on a 12v battery supply.

...

    The software works like this: #!/usr/bin/python3 makes sure I run a python3 software package w/ sudo ./Tester.py.
    Now...I import the GPIO library from Adafruit_BBIO. I also import time. I call my specific pins on the LoadCape
    by their respective values. Then, I create an empty instance. I set up GPIO and label my called pin values by 
    name, i.e. Master_Pin1 and etc...

    Then, I call a while function as True. This makes sure my software in my while function will run repeatedly until
    I cancel my program or something negative happens to the software or hardware. 

    GPIO.output is the way to tell the machine which pin to use and if the pin will be high or low. By calling my pin 
    high, I am able to run a specific motor from the below set up of lead connections and the LoadCape.
    time.sleep(value) or time.sleep(int) or time.sleep(5) is telling my machin to run that many seconds while the pin is
    set to high/on. When I call the pin low, it runs and turns the pin low/off w/ GPIO.output.

If you are using a GND, which you should always use, try Sink1 on your LoadCape. A small battery can run your LoadCape and if you are powering
motors, you can power those separately w/ the positive leads going to VIN while the motor GND wiring goes to Sink1.

...

    So, say this is your motor: positive & negative
                                |          |
                                |          goes to Sink1 on the LoadCape
                                | 
                                goes to battery1

Do not forget to power your LoadCape w/ an additional battery supply. 

...

Or...

    So, say this is your motor: positive & negative
                                |          |
                                |          Sink1
                                |
                                VIN on the LoadCape

Oh and you can use sys_5v from your BBB to power the board for testing if necessary but please remember to to power the Cape w/
another form of power supply (battery) so that the motor(s) have a way to get power.

Seth

P.S. LOADCAPE!
