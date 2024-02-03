#!/usr/bin/python3

# Getting help from #beagle on IRC
# You know who you are currently!

from pathlib import Path
from time import sleep

class Gpio:
    def __init__(self, name):
        self.name = name
        self._value_path = Path('/sys/class/leds/', name, 'brightness')
        # While /sys/class/leds/brightness is the gpio in question, load-sink1 is used as name...
        # This is part of the new specification from beagleboard.org. 
        # So, something like this will be available when the Cape is attached:
            # /sys/class/leds/load-sink(N)/brightness where (N) is the listed load to use!
            # GPIO!
    def get(self):
        return int(self._value_path.read_text())

    def set(self, value):
        self._value_path.write_text(str(value))

relay2 = Gpio('load-sink1')
# The name relay2 relates to a different cape called the Relay Cape. 
# This labeling scheme can be changed to suit your needs, e.g. load1, load2, load3, and etc.
relay2.set(1)
sleep(2)
relay2.set(0)
sleep(2)
