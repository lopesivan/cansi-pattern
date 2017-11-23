#ifndef BLINK_H
#define BLINK_H

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct blink* blinkPtr;

blinkPtr createLed (void);
void destroyLed (blinkPtr instance);

void ligaLed (blinkPtr instance);
void desligaLed  (blinkPtr instance);

#endif
