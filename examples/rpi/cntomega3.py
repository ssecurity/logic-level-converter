#!/usr/bin/env python
# -*- coding: utf-8

import serial
import cgi
import time

try:
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    while 1 :
	ser.write('HELLO FROM RPI.V1B\n')
	time.sleep(5)
except MySQLdb.Error:
    print("Some  Error")
