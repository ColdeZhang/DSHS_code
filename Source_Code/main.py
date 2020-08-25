"""
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
    Main script

@Description:
        Host's source code of DSHS, 
    running on Raspberry Pi. Using SPI
    protocol to communicate with Units.

@Pin map:
    BOARD#31 > (EN1)EN_1
    BOARD#32 > (EN2)EN_2
    BOARD#33 > (SS3)74HC138_1_A2
    BOARD#35 > (SS2)74HC138_1_A1
    BOARD#37 > (SS1)74HC138_1_A0
    BOARD#33 > (SS6)74HC138_2_A2
    BOARD#35 > (SS5)74HC138_2_A1
    BOARD#37 > (SS4)74HC138_2_A0
     
===========================================
"""

# import libraries
import RPi.GPIO as GPIO
import spidev
import time
import chipCtrl

# GPIO constants
hub = [31, 33, 35, 37, 32, 36, 38, 40]


# board pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
for i in len(hub):
    GPIO.setup(hub[i], GPIO.OUT)

# initialze SPI
spi = spidev.SpiDve()
spi.open(0, 0)
spi.max_speed_hz = 7800000
msgPrint('SPI initialization success.')

# print and display system
def msgPrint(msg):
    print('Sys_>' + msg)

# main circul function
try:
    while True:
        msgPrint('sys running......')

        
except KeyboardInterrupt:
    spi.close()
    GPIO.cleanup()