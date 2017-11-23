#include "TrigCategories.h"

/* In production code, I would definitely validate all input and
   secure the calculations upon entry of each function... */

double hipoPitagorasStrategy (double a,double b)
{
    return a^2+b^2;
}
double catPitagorasStrategy (double a,double b)
{
    return a^2-b^2;
}
