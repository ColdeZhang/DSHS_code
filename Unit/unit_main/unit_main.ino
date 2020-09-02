/*
===========================================
         ____  ____  _   _ ____  
        |  _ \/ ___|| | | / ___| 
        | | | \___ \| |_| \___ \ 
        | |_| |___) |  _  |___) |
        |____/|____/|_| |_|____/ 

      Deer  Smart   Home    System

@Author:
    Unlimited_Deer_

@Type
    Unit main script

@Description:
        Unit's source code of DSHS, 
    running on Mega 2560. Using SPI
    protocol to communicate with Hosts.
===========================================
*/

#include <SPI.h>

void setup() {
  
  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);

  // turn on SPI in slave mode
  SPCR |= _BV(SPE);
  
}

void loop() {
  // put your main code here, to run repeatedly:

}
