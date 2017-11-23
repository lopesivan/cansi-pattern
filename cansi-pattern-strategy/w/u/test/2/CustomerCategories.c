#include "CustomerCategories.h"

/* In production code, I would definitely validate all input and
   secure the calculations upon entry of each function... */

double hipoTrigStrategy (double a,double b)
{
    return a^2+b^2;
}
double catTrigStrategy (double a,double b)
{
    return a^2-b^2;
}
