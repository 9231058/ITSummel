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
delay = 5

while True:
    voice_level = ReadChannel(voice_channel)

    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    time.sleep(0.3)
    print(voice_level)

    # Yellow
    if (int(voice_level) < 200):
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        # time.sleep(0.3)

    # Green
    if int(voice_level) > 200 and voice_level < 600:
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)
        # time.sleep(0.3)

    # Red
    if int(voice_level) > int("600") and voice_level < int("1000"):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
        # time.sleep(0.3)

    # Yellow
    if int(voice_level) > int("1000"):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        # time.sleep(0.3)
