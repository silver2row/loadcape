# Load Cape

Hello...this is GHI's Load Cape from BeagleBoard.org.

# Starter Software listed in the above files can be used on the BeagleBone Black and other am335x processor related boards from beagleboard.org.
`As things change in time, docs.beagleboard.org can be used to update ideas...`

    So, say this is your motor: positive & negative & GND
                                           |           |
                                           |           GND
                                           - Sink1
                                |
                                - VIN on the Load Cape while the positive
                                - lead from the battery goes into the VIN
                                - screw terminal on the Load Cape too.

P.S. Load Cape, this Cape can also be used for the BeagleV-Ahead which has a th1520 quad-core processor (c910).

`One key difference between using .dtbo files for the separate boards, BBB and BeagleV-Ahead, is that the BBB uses uEnv.txt in u-boot to handle .dtbo files while the BeagleV-Ahead uses extlinux.conf to account for the .dtbo files.`
