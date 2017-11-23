#include "WatchState.h"
#include "WatchStateInternal.h"

#include "message.h" // DEBUG

/*
Provide the default implementations:
*/

static void defaultStop (WatchStatePtr state)
{
    message ("** defaultStop **");

    /* We'll get here if the stop event isn't supported
       in the concrete state. */
}

static void defaultStart (WatchStatePtr state)
{
    message ("** defaultStart **");

    /* We'll get here if the start event isn't supported
       in the concrete state. */
}


void defaultImplementation (WatchStatePtr state)
{
    message ("** defaultImplementation **");

    state->start = defaultStart;
    state->stop  = defaultStop;

}
