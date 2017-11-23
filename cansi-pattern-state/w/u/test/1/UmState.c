#include "UmState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "DoisState.h"

#include "message.h" // DEBUG

static void doisEstado (EstadoStatePtr state)
{
    message ("** doisEstado **");

    transitionToDois (state);
}

void transitionToUm (EstadoStatePtr state)
{
    message ("** transitionToUm **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->dois = doisEstado;
}
