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
    Function library

@Description:
        This script used to control some 
    digital logic chips. 
        Chips supported: 
        >>74HC138
     
===========================================
"""

import RPi.GPIO as GPIO
import math

def gpioInit():
    '''Initialize GPIO with BOARD mode.'''
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()

def gpioOutInit(pin: list):
    '''Set pin with OUT mode'''
    for i in range(len(pin)):
        GPIO.setup(pin[i], GPIO.OUT)

def gpioInInit(pin: list):
    '''Set pin with IN mode'''
    for i in range(len(pin)):
        GPIO.setup(pin[i], GPIO.IN)

def HC138(pin_map: list, port_ID: int):
    '''control 74HC138 digital logic chips; pin_map[En, A2, A1, A0, ......]; port_ID starts from 0 '''
    # ep: pin_map[En, A2, A1, A0]
    #[31, 33, 35, 37, 32, 36, 38, 40]
    # 0   1   2   3   4   5   6   7   8   9   10   11
    # ^               ^               ^        
    # port_ID start from '0'

    chip_num = len(pin_map) / 4 # numbers of chips
    '''isinstance(chip_num, int)''' 
    if math.modf(chip_num)[0] == 0:
        if -1 < port_ID < (chip_num * 8 + 1):
            # set all chips to disable mode
            for i in range(chip_num):
                GPIO.output(pin_map[(i - 1) * 4], GPIO.LOW)
            chips_port_ID = port_ID % 8 # (0~7)
            chips_ID = int(port_ID / 8) # start from 0
            # enable required chip
            GPIO.output(pin_map[chips_ID * 4], GPIO.HIGH)
            if chips_port_ID == 0:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.LOW)
            elif chips_port_ID == 1:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.HIGH)
            elif chips_port_ID == 2:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.LOW)
            elif chips_port_ID == 3:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.HIGH)
            elif chips_port_ID == 4:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.LOW)
            elif chips_port_ID == 5:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.LOW)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.HIGH)
            elif chips_port_ID == 6:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.LOW)
            elif chips_port_ID == 7:
                GPIO.output(pin_map[chips_ID * 4 + 1], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 2], GPIO.HIGH)
                GPIO.output(pin_map[chips_ID * 4 + 3], GPIO.HIGH)
        else:
            return msgPrint('error: port ID out of the range of 74HC138 chips!')
    else:
        return msgPrint('error: pin map input wrong, check the input list')


def msgPrint(msg):
    '''print and display system'''
    print('Sys_>' + msg)
    