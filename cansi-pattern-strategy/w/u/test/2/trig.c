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

TrigPtr createTrig
 (const char* name, const Address* address, CustomerPriceStrategy priceStrategy)
{
    TrigPtr trig = malloc (sizeof *trig);

    if (NULL != trig)
    {
        /* Bind the initial strategy supplied by the client. */
        trig->pitagorasStrategy = PitagorasStrategy;
        /* Initialize the other attributes of the customer here. */
    }

    return trig;
}

void destroyTrig (TrigPtr trig)
{
    /* Perform clean-up of the trig internals, if necessary. */
    free (trig);
}

void changePitagorasCategory()
{
    trig->pitagorasStrategy = newPitagorasStrategy;
}
