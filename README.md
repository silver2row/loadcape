# Load Cape

Hello...this is the Load Cape.

# Starter Software and Ideas
`As things change in time, docs.beagleboard.org can be used to update ideas...`

```
    So, say this is your motor: positive & negative
                                |            |          
                                |            |
                                |            - Sink1
                                |
                                - VIN on the Load Cape while the positive
                                  lead from the battery goes into the VIN
                                  screw terminal on the Load Cape too.

                                - Battery GND goes to Load Cape GND
```

P.S. Load Cape, this Cape can also be used for the BeagleV-Ahead which has a th1520 quad-core processor (c910). I
think this Load Cape can also be used with the BeagleBone-AI64 which has dual-core, Cortex-A72s on the TDA4VM.

```
For the BBAI-64, use this kernel:
Linux BeagleBone-AI64 5.10.168-ti-arm64-r113 
#1bookworm SMP Sun Dec 17 00:12:52 UTC 2023 aarch64 GNU/Linux

and this image:
BeagleBoard.org Debian Bookworm Minimal Image 2023-10-07
```

I have found both the 5.10.168-ti-arm64-r113 kernel from beagleboard.org and the
Bookworm image 2023-10-07 work with the Load Cape. 

Seth

P.S. If you have any questions, do not hesitate to ask to prompt me or steal away ideas!
