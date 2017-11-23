#include "blink.h"

/* We need to know about or initial state: */
#include "DesligaState.h"

#include "LedStateInternal.h"
#include <stdlib.h>

#include "message.h" // DEBUG

struct blink
{
    struct LedState state;
};

/* Estatico */
/* USING:
    blinkPtr p = createLed();
    ligaLed(p);
*/
#define MAX_NO_OF_BLINKS 2
static struct blink objectPool[MAX_NO_OF_BLINKS];
static size_t numberOfObjects = 0;

blinkPtr createLed (void)
{
    message("** createLed **");

    blinkPtr instance = NULL;

    if (numberOfObjects < MAX_NO_OF_BLINKS)
    {
        instance = &objectPool[numberOfObjects++];
        /* Initialize the object... */

        /* Specify the initial state. */
        transicaoParaDesliga (&instance->state);
        /* Initialize the other attributes here.*/
    }

    return instance;
}

/* Dinamico */
/* USING:
    blinkPtr p = createLed();
    ligaLed(p);
*/
/*
blinkPtr createLed (void)
{
    message("** createLed **");

    blinkPtr instance = malloc (sizeof *instance);

    if (NULL != instance)
    {
        transicaoParaDesliga (&instance->state);
    }
    return instance;
}
*/

void destroyLed (blinkPtr instance)
{
    message("** destroyLed **");

    free (instance);
}

void ligaLed (blinkPtr instance)
{
    /*
    message("** ABSTRACT: ligaLed **");
    */
    instance->state.liga (&instance->state);
}

void desligaLed (blinkPtr instance)
{
    /*
    message("** ABSTRACT: desligaLed **");
    */

    instance->state.desliga (&instance->state);
}

