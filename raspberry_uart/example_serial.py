#!/usr/bin/env python
import time
import serial
import array as arr
import numpy as np
import codecs
import struct

TT_vol2 = bytes([0XF1, 0x00])

TT_vol = arr.array('B', [0XF1, 0x00])
TT_cur = arr.array('B', [0xF2, 0x00])
TT_frq = arr.array('B', [0xF3, 0x00])
TT_enr = arr.array('B', [0xF4, 0x00])
TT_pow = arr.array('B', [0xF5, 0x00])
TT_pf  = arr.array('B', [0xF6, 0x00])

KDL_float = 0x0A
KTD_float = 0x04
TTCB3 = 0x03
TTCB1 = 0x01


class Node:
    def __init__(self, SRG, SRN, amountSensor):
        self.SRG = SRG
        self.SRN = SRN
        self.amountSensor = amountSensor
    

    def request(self, MBT, ser, SLT):
        #dataSend.append(MTB%256)
        ch = 'c'
        #chOut = codecs.encode(ch, "hex")
        dataSend = arr.array('B', [int(MBT/256), int(MBT%256), 0x0A])
        dataSend += arr.array('B', [0x45, 0x4D, 0X47, 0X4C, 0X00])
        dataSend += arr.array('B', [0x45, 0x4D, 0X4E, 0X33, 0X4C])
        listSRG = list(self.SRG)
        listSRN = list(self.SRN)
        for i in range(0,7):
            dataSend.append(ord(listSRG[i]))
        for i in range(0,7):
            dataSend.append(ord(listSRN[i]))    
        if SLT == 1:
            dataSend.append(SLT)
                
            dataSend += TT_vol                
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)                
                
            dataSend += TT_cur
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)
                
            dataSend += TT_frq
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)
            
            dataSend += TT_enr
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)
            
            dataSend += TT_pow
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)
            
            dataSend += TT_pf
            dataSend.append(KDL_float)
            dataSend.append(KTD_float)
            dataSend.append(0)
            
        if SLT == 3:
            dataSend.append(SLT)
            for i in range(0,2):
                dataSend += TT_vol
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)                
            
                dataSend += TT_cur
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)
            
                dataSend += TT_frq
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)
            
                dataSend += TT_enr
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)
            
                dataSend += TT_pow
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)
            
                dataSend += TT_pf
                dataSend.append(KDL_float)
                dataSend.append(KTD_float)
                dataSend.append(i)
            
        print ("dataSend = ", end = '')
        for i in range(0,len(dataSend)):
            print (hex(dataSend[i]), end = ' ')
        print ("-----------------")
        ser.write(dataSend)
        ser.flush()

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5
)

while 1:
    dataReceive = ser.read(200)
    lenData = len(dataReceive)
    if lenData!=0:
        for i in range(0,lenData):
            y = dataReceive[i]
            print (hex(dataReceive[i]), end = ' ')
        print ()
        print ("lenngth(x) = ",lenData)
    
        print ("-----------------")
        node = Node("87654321", "12345678", 1)
        MBT = 2345
        node.request(MBT,ser, 1)
        
        MBT_N = dataReceive[0:2]
#         LBT_N = arr.array('B', [dataReceive[3]])
        LBT_N = dataReceive[2]
        MTBG_N = dataReceive[3:8]
        MTBN_N = dataReceive[8:13]
        SRG_N = dataReceive[13:21]
        SRN_N = dataReceive[21:29]
#         SLT_N = arr.array('B', [dataReceive[30]])
        SLT_N = dataReceive[29]
        
        
#         for i in range(0,2):
#             TT_N[i] = dataReceive[i]
        print("data MBT is: ", MBT_N.hex())
        print("data LBT is: ", hex(LBT_N))
        print("data MTBG is: ", MTBG_N.hex())
        print("data MTBN is: ", MTBN_N.hex())
        print("data SRG is: ", SRG_N.hex())
        print("data SRN is: ", SRN_N.hex())
        print("data SLT is: ", hex(SLT_N))
        
        m = 30
        
        for i in range(0, SLT_N):
#         for i in range(0, 1):
            TT_N = dataReceive[m:m+2]
            KDL_N = dataReceive[m+2]
            KTD_N = dataReceive[m+3]
            TTCB = dataReceive[m+4]
            DAT = dataReceive[m+5:m+5+KTD_N]
            
            
            m = m + 5 + KTD_N
            print("---------------")
            
            temp = arr.array('B', TT_N)
            
            print("data TT_N is: ", TT_N.hex(), end = '' )
            if(temp == TT_vol):
                print (" - DIEN AP")
            if(temp == TT_cur):
                print (" - CUONG DO")
            if(temp == TT_frq):
                print (" - TAN SO")
            if(temp == TT_enr):
                print (" - NANG LUONG")
            if(temp == TT_pow):
                print (" - CONG SUAT")
            if(temp == TT_pf):
                print (" - HE SO CONG SUAT")
            
            print("data KDL_N is: ", hex(KDL_N), end = '' )
            if(KDL_N == 0x0A):
                print (" - float")
            print("data KTD_N is: ", hex(KTD_N))
            print("data TTCB is: ", hex(TTCB))
            print("data DAT is: ", DAT.hex())
#             print("m= ", m)            
            
            if((KTD_N == 4) and (KDL_N == 0x0A)):
                valueDAT = 0.0
                valueDAT = struct.unpack('f', DAT)
                print("Float value DAT= ", valueDAT)
            print("---------------")
	
