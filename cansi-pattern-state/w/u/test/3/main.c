#include <stdlib.h>
#include <stdio.h>

#include "DigitalStopWatch.h"

/*****************************************************************************
 *                                                                           *
 *  --------------------------------- main --------------------------------- *
 *                                                                           *
 *****************************************************************************/

int
main (int argc, char *argv[])
{

    DigitalStopWatchPtr p = createWatch();
    startWatch (p);

    stopWatch (p);

    return EXIT_SUCCESS;
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */
