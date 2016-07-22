#!/usr/bin/env python3
# In The Name Of God
# ========================================
# [] File Name : mic.py
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
GPIO.setup(15, GPIO.IN)
try:
    while True:
        print(GPIO.input(15))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Thank you for using 18.20 :)")
