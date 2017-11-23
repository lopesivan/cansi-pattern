#include "DesligaState.h"
#include "LedStateInternal.h"

/* Possible transition to the following state: */
#include "LigaState.h"

#include "message.h" // DEBUG

static void ligaLed (LedStatePtr state)
{
    message("** ligaLed **");

    transicaoParaLiga (state);
}

void transicaoParaDesliga (LedStatePtr state)
{
    message("** transicaoParaDesliga **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the stoped
       state. */

    implementacaoPadrao (state);
    state->liga = ligaLed;
}

