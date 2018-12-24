# loadcape

...

Hello...this is GHI's LoadCape w/ BeagleBoard.org. GHI manufactured it.

Anyway...

# Starter Software

...

I have listed some starter software for your LoadCape.

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
