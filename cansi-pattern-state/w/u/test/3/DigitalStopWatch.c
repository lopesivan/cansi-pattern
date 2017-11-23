#include "DigitalStopWatch.h"

/* We need to know about or initial state: */
#include "StopState.h"

#include "WatchStateInternal.h"
#include <stdlib.h>

#include "message.h" // DEBUG

struct DigitalStopWatch
{
    struct WatchState state;
};

/* Estatico */
/* USING:
    DigitalStopWatchPtr p = createWatch();
    startWatch(p);
*/
#define MAX_NO_OF_DIGITALSTOPWATCHS 2
static struct DigitalStopWatch objectPool[MAX_NO_OF_DIGITALSTOPWATCHS];
static size_t numberOfObjects = 0;

DigitalStopWatchPtr createWatch (void)
{
    message ("** createWatch **");

    DigitalStopWatchPtr instance = NULL;

    if (numberOfObjects < MAX_NO_OF_DIGITALSTOPWATCHS)
    {
        instance = &objectPool[numberOfObjects++];
        /* Initialize the object... */

        /* Specify the initial state. */
        transitionToStop (&instance->state);
        /* Initialize the other attributes here.*/
    }

    return instance;
}

/* Dinamico */
/* USING:
    DigitalStopWatchPtr p = createWatch();
    startWatch(p);
*/
/*
DigitalStopWatchPtr createWatch (void)
{
    message("** createWatch **");

    DigitalStopWatchPtr instance = malloc (sizeof *instance);

    if (NULL != instance)
    {
        transitionToStop (&instance->state);
    }
    return instance;
}
*/

/*
void statemachine(void)
{
    message("** statemachine **");

    DigitalStopWatchPtr instance = NULL;

    if (numberOfObjects < MAX_NO_OF_DIGITALSTOPWATCHS)
    {
        instance = &objectPool[numberOfObjects++];

        transitionToStop (&instance->state);

        while(1)
        {
            instance->state.func (&instance->state);
        }
    }
}
*/

void destroyWatch (DigitalStopWatchPtr instance)
{
    message ("** destroyWatch **");

    free (instance);
}

void startWatch (DigitalStopWatchPtr instance)
{
    /*
    message("** ABSTRACT: startWatch **");
    */
    instance->state.start (&instance->state);
}

void stopWatch (DigitalStopWatchPtr instance)
{
    /*
    message("** ABSTRACT: stopWatch **");
    */

    instance->state.stop (&instance->state);
}

