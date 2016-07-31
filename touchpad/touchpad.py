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
import requests

# Setup library configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Trun GPIO15 on
GPIO.setup(14, GPIO.IN)
try:
    while True:
        try:
            GPIO.wait_for_edge(14, GPIO.RISING)
        except RuntimeError:
            pass
        print("Someone touched me :(")
        requests.get('http://thingtalk.ir/update', data={'key': '4W8IN7UU92XNWKWQ', 'field1': '1'})
except KeyboardInterrupt:
    pass
finally:
    print("Thank you for using 18.20 :)")
