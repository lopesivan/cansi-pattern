#ifndef TRIG_H
#define TRIG_H

#include "CustomerStrategy.h"
#include "Address.h"

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct Trig* TrigPtr;

/*
Create a Trig and return a handle to it.
*/
TrigPtr createTrig (const char* name, const Address* address, CustomerPriceStrategy priceStrategy);

/*
Destroy the given Trig object.
All handles to it will be invalidated.
*/
void destroyTrig
    (TrigPtr trig);

void changePitagorasCategory();
#endif
