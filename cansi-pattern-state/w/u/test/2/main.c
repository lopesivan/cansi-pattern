#include <stdlib.h>
#include <stdio.h>

#include "blink.h"

/*****************************************************************************
 *                                                                           *
 *  --------------------------------- main --------------------------------- *
 *                                                                           *
 *****************************************************************************/

int
main (int argc, char *argv[]) {

    blinkPtr p = createLed();
    ligaLed(p);
    desligaLed(p);

    ligaLed(p);
    desligaLed(p);

    return EXIT_SUCCESS;
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */
