#include "StartState.h"
#include "WatchStateInternal.h"

/* Possible transition to the following state: */
#include "StopState.h"

#include "message.h" // DEBUG

static void stopWatch (WatchStatePtr state)
{
    message ("** stopWatch **");

    transitionToStop (state);
}

void transitionToStart (WatchStatePtr state)
{
    message ("** transitionToStart **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the started
       state. */

    defaultImplementation (state);
    state->stop = stopWatch;
    /*state->func = stopWatch;*/
}

