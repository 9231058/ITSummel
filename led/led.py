#!/usr/bin/env python3
# In The Name Of God
# ========================================
# [] File Name : led.py
#
# [] Creation Date : 17-07-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import RPi.GPIO as GPIO
import time

# Setup library configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Trun GPIO15 on
GPIO.setup(15, GPIO.OUT)
try:
    while True:
        GPIO.output(15, True)
        time.sleep(1)
        GPIO.output(15, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.output(15, False)
    print("Thank you for using 18.20 :)")
