// Taken from docs.beagleboard.org under the header /boards/capes/relay.rst
// toggle1.c is the file in question!

// the file has moved from so-said dir and file.
// I will research where it is located again and get back to you!

#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

#define CONSUMER    "Load"

int main(int argc, char **argv)
{
    int chipnumber = 1;
    struct gpiod_chip *chip;
    struct gpiod_line *line;

    int i, ret;

    // Open GPIO chip
    chip = gpiod_chip_open_by_number(chipnumber);
    if (!chip) {
        perror("Open chip failed\n");
        return 1;
    }

    // Open GPIO lines
    line = gpiod_chip_get_line(chip, 123);
    if (!line) {
        perror("Get line failed\n");
        return 1;
    }

    // Open LED lines for output
    ret = gpiod_line_request_output(line, CONSUMER, 0);
    if (ret < 0) {
        perror("Requested line as output failed\n");
        return 1;
    }

    // Turn on Load (Motor) and Move it!
    i = 0;
    while (true) {
        ret = gpiod_line_set_value(line, (i & 1) != 0);
        if (ret < 0) {
            perror("Set line output failed\n");
            return 1;
        }
        usleep(1000000);
        i++;
    }

// Release lines and chip
release_line:
    gpiod_line_release(line);
close_chip:
    gpiod_chip_close(chip);
end:
    return 0;
}
