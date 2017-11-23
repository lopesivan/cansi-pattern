#include "contexto.h"

/* We need to know about or initial state: */
#include "TresState.h"

#include "EstadoStateInternal.h"
#include <stdlib.h>

#include "message.h" // DEBUG

struct contexto
{
    struct EstadoState state;
};

/* Estatico */
/* USING:
    contextoPtr p = createEstado();
    umEstado(p);
*/
#define MAX_NO_OF_CONTEXTOS 2
static struct contexto objectPool[MAX_NO_OF_CONTEXTOS];
static size_t numberOfObjects = 0;

contextoPtr createEstado (void)
{
    message ("** createEstado **");

    contextoPtr instance = NULL;

    if (numberOfObjects < MAX_NO_OF_CONTEXTOS)
    {
        instance = &objectPool[numberOfObjects++];
        /* Initialize the object... */

        /* Specify the initial state. */
        transitionToTres (&instance->state);
        /* Initialize the other attributes here.*/
    }

    return instance;
}

/* Dinamico */
/* USING:
    contextoPtr p = createEstado();
    umEstado(p);
*/
/*
contextoPtr createEstado (void)
{
    message("** createEstado **");

    contextoPtr instance = malloc (sizeof *instance);

    if (NULL != instance)
    {
        transitionToTres (&instance->state);
    }
    return instance;
}
*/

void destroyEstado (contextoPtr instance)
{
    message ("** destroyEstado **");

    free (instance);
}

void umEstado (contextoPtr instance)
{
    /*
    message("** ABSTRACT: umEstado **");
    */
    instance->state.um (&instance->state);
}

void tresEstado (contextoPtr instance)
{
    /*
    message("** ABSTRACT: tresEstado **");
    */

    instance->state.tres (&instance->state);
}

void doisEstado (contextoPtr instance)
{
    /*
    message("** ABSTRACT: doisEstado **");
    */

    instance->state.dois (&instance->state);
}

void proximo (contextoPtr instance) {
    umEstado(instance);
    doisEstado(instance);
    tresEstado(instance);
}