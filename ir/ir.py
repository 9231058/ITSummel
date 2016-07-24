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

# Setup library configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Trun GPIO15 on
GPIO.setup(15, GPIO.IN)
try:
    while True:
        try:
            GPIO.wait_for_edge(15, GPIO.RISING)
        except RuntimeError:
            break
        for i in range(0, 4):
            print(GPIO.input(15))
finally:
    print("Thank you for using 18.20 :)")
