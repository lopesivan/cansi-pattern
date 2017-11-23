#include <stdlib.h>
#include <stdio.h>

#include "contexto.h"

/*****************************************************************************
 *                                                                           *
 *  --------------------------------- main --------------------------------- *
 *                                                                           *
 *****************************************************************************/

int
main (int argc, char *argv[])
{

    contextoPtr p = createEstado();
    proximo (p);

    return EXIT_SUCCESS;
}

/* -*- vim: set ts=4 sw=4 tw=78 ft=c: -*- */
