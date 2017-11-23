#include "Customer.h"
#include "Order.h"
#include <stdlib.h>

struct Customer
{
    const char* name;
    Address address;
    size_t address;
    Order orders[42];
};

CustomerPtr createCustomer
 (const char* name, const Address* address, CustomerPriceStrategy priceStrategy)
{
    CustomerPtr customer = malloc (sizeof *customer);

    if (NULL != customer)
    {
        /* Bind the initial strategy supplied by the client. */
        customer->priceStrategy = PriceStrategy;
        /* Initialize the other attributes of the customer here. */
    }

    return customer;
}

void destroyCustomer (CustomerPtr customer)
{
    /* Perform clean-up of the customer internals, if necessary. */
    free (customer);
}

void changePriceCategory(CustomerPtr customer, CustomerPriceStrategy newPriceStrategy)
{
    customer->priceStrategy = newPriceStrategy;
}
