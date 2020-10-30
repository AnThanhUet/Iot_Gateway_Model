#!/usr/bin/env python
import time
import serial
import array as arr
import numpy as np
import codecs
import struct

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.1
)

while 1:
    dataReceive = ser.read(200)
    lenData = len(dataReceive)
    if lenData!=0:
        for i in range(0,lenData):
            y = dataReceive[i]
        print ()
        print ("-----------------")
        print ("lenngth(x) = ",lenData)
        print ("dataReceive = ",dataReceive)
        print ("kieu data y", type(y))
        print ("y = "+ str(y))
        print("---------------")
    

