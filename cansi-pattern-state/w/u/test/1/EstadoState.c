#include "EstadoState.h"
#include "EstadoStateInternal.h"

#include "message.h" // DEBUG

/*
Provide the default implementations:
*/

static void defaultTres (EstadoStatePtr state)
{
    message ("** defaultTres **");

    /* We'll get here if the stop event isn't supported
       in the concrete state. */
}

static void defaultUm (EstadoStatePtr state)
{
    message ("** defaultUm **");

    /* We'll get here if the start event isn't supported
       in the concrete state. */
}

static void defaultDois (EstadoStatePtr state)
{
    message ("** defaultDois **");
    /* We'll get here if the start event isn't supported
       in the concrete state. */
}

void defaultImplementation (EstadoStatePtr state)
{
    message ("** defaultImplementation **");

    state->um = defaultUm;
    state->tres  = defaultTres;

    state->dois = defaultDois;
}
