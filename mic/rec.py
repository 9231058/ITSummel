#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import spidev

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Open SPI bus 0 for device 0
spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    '''
    Function to read SPI data from MCP3008 chip
    channel must be integer between 0 and 7
    '''
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

# Define sensor channels
voice_channel = 0

# Define delay between readings
delay = 0.1
wav = open('sound.wav', 'w')

try:
    while True:
        voice_level = ReadChannel(voice_channel)
        time.sleep(delay)
        print(voice_level)
        wav.write(bytes(voice_level))
except KeyboardInterrupt:
    wav.close()
