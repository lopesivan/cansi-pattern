#include "LedState.h"
#include "LedStateInternal.h"

#include "message.h" // DEBUG

/*
Provide the default implementations:
*/

static void defaultDesliga (LedStatePtr state)
{
    message("** defaultDesliga **");

    /* We'll get here if the stop event isn't supported
       in the concrete state. */
}

static void defaultLiga (LedStatePtr state)
{
    message("** defaultLiga **");

    /* We'll get here if the start event isn't supported
       in the concrete state. */
}


void implementacaoPadrao (LedStatePtr state)
{
    message("** implementacaoPadrao **");

    state->liga = defaultLiga;
    state->desliga = defaultDesliga;

}
