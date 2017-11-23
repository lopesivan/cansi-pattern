#include "LigaState.h"
#include "LedStateInternal.h"

/* Possible transition to the following state: */
#include "DesligaState.h"

#include "message.h" // DEBUG

static void desligaLed (LedStatePtr state)
{
    message("** desligaLed **");

    transicaoParaDesliga (state);
}

void transicaoParaLiga (LedStatePtr state)
{
    message("** transicaoParaLiga **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    implementacaoPadrao (state);
    state->desliga = desligaLed;
}

