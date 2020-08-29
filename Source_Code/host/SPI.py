import spidev

def spiInit():
    '''Initialze SPI protocol'''
    spi = spidev.SpiDve()
    spi.open(0, 0)
    spi.max_speed_hz = 7800000