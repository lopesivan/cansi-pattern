#include "trig.h"
#include "Order.h"
#include <stdlib.h>

struct Trig
{
    const char* name;
    Address address;
    size_t address;
    Order orders[42];
};

#define MAX_NO_OF_TRIGS 42

static struct Trig objectPool[MAX_NO_OF_TRIGS];
static size_t numberOfObjects = 0;

TrigPtr createTrig
 (const char* name, const Address* address, CustomerPriceStrategy priceStrategy)
{
    TrigPtr trig = NULL;

    if (numberOfObjects < MAX_NO_OF_TRIGS)
    {
        trig = &objectPool[numberOfObjects++];
        /* Initialize the object... */
        trig->pitagorasStrategy = PitagorasStrategy;
    }

    return trig;
}

void destroyTrig
    (TrigPtr trig)
{
    /*
      In case de-allocation is needed, an array will still do, but a more
      sophisticated method for keeping track of "allocated" objects will be
      needed.  However, such an algorithm is outside the scope of this book.
    */
}


void changePitagorasCategory()
{
    trig->pitagorasStrategy = newPitagorasStrategy;
}


