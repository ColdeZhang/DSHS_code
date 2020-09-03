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
    SPI protocol script

@Description:
        This script controlling SPI protocol
    to communicate with Hosts.
     
===========================================
"""

import spidev

def spiInit():
    '''Initialze SPI protocol'''
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 7800000

def transfer(jsonData):
    '''Execute spi transfer and return a json from units (slave devices)'''
    bytesData = json2bytes(jsonData)
    rcvd = spi.xfer(bytesData)
    jsonData = bytes2json(rcvd)
    return jsonData


def json2bytes(jsonData):
    '''Convert json data to bytes data.'''
    bytesData = null
    return bytesData

def bytes2json(bytesData: list):
    '''Convert bytes data to json data'''
    jsonData = null
    return jsonData


    