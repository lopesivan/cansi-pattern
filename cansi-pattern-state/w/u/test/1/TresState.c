#include "TresState.h"
#include "EstadoStateInternal.h"

/* Possible transition to the following state: */
#include "UmState.h"

#include "message.h" // DEBUG

static void umEstado (EstadoStatePtr state)
{
    message ("** umEstado **");

    transitionToUm (state);
}

void transitionToTres (EstadoStatePtr state)
{
    message ("** transitionToTres **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the stoped
       state. */

    defaultImplementation (state);
    state->um = umEstado;
    /*state->func = umEstado;*/
}

