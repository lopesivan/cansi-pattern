#include "StopState.h"
#include "WatchStateInternal.h"

/* Possible transition to the following state: */
#include "StartState.h"

#include "message.h" // DEBUG

static void startWatch (WatchStatePtr state)
{
    message ("** startWatch **");

    transitionToStart (state);
}

void transitionToStop (WatchStatePtr state)
{
    message ("** transitionToStop **");

    /* Initialize with the default implementation before
       specifying the events to be handled in the stoped
       state. */

    defaultImplementation (state);
    state->start = startWatch;
    /*state->func = startWatch;*/
}

