#!/usr/bin/env python
# -*- coding: utf-8

import serial
import cgi

try:
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    while 1 :
        a = ser.readline()
        a = a.replace("\n",'')
        a = a.replace("\r",'')
        a = "'"+a.replace("'","''")+"'"
        print('INSERT INTO `sessionlog` (`message`,`dt`) VALUES ('+a+', now())')
except MySQLdb.Error:
    print("Some  Error")
