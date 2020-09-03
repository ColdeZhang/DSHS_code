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
  Serial.begin(115200);
  
  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);

  // turn on SPI in slave mode
  SPCR |= _BV(SPE);
  
}

// SPI interrupt routine
ISR (SPI_STC_vect)
{
  byte c = SPDR;
  Serial.println(c);
  SPDR = c+10;
}  // end of interrupt service routine (ISR) for SPI

void loop() {
  

}
