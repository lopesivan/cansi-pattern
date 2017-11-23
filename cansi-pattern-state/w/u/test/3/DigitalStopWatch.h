#ifndef DIGITAL_STOP_WATCH_H
#define DIGITAL_STOP_WATCH_H

/*
A pointer to an incomplete type (hides the implementation details).
*/
typedef struct DigitalStopWatch* DigitalStopWatchPtr;

DigitalStopWatchPtr createWatch (void);
void destroyWatch (DigitalStopWatchPtr instance);

void startWatch (DigitalStopWatchPtr instance);
void stopWatch  (DigitalStopWatchPtr instance);

/*
void statemachine(void);
*/

#endif
