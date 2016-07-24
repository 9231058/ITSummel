#!/usr/bin/env python3
# In The Name Of God
# ========================================
# [] File Name : ir.py
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
t = 0
try:
    while True:
            if(GPIO.input(15)):
                t += 0.5
            else:
                print(t)
                t = 0
            time.sleep(0.5)
finally:
    print("Thank you for using 18.20 :)")
