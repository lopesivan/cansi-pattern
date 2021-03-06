#ifndef LED_STATE_INTERNAL_H
#define LED_STATE_INTERNAL_H

/*
 We need a shared definition of our incomplete type
 exposed in the API. One strategy is to define it
 in an include file like this that we can share
 between the different translation units.
 The advantage is that we keep the definition out
 of the API.
*/

/* Simplify the code by using typedefs for the function pointers. */
typedef void (*EventLigaFunc) (LedStatePtr);
typedef void (*EventDesligaFunc)  (LedStatePtr);

struct LedState
{
    EventLigaFunc liga;
    EventDesligaFunc desliga;
};

#endif
