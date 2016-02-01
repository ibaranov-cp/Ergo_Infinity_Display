#!/usr/bin/env python

# Author: Nick Choi


import wmi
import os
import psutil
from time import strftime, time
import urllib
import socket

from Ergo_Infinity_Display import *

lcd = [[0 for x in range(32)] for x in range(128)]

w = wmi.WMI(namespace='root\\wmi')
hostname = socket.gethostname()

test = "test string to scroll"

if __name__ == '__main__':

    ser = serial.Serial('COM3', 115200, timeout=0.5)  # Change to (Serial port - 1) on Windows.
    ser.close()
    ser.open()



    # Get external IP once (Not ideal....)
    ip = urllib.urlopen('http://whatismyip.org').read()  # External IP, This may need to be fixed as website changes
    p = ip.find("font-weight: 600;")
    ip = ip[p + 19:p + 34].strip('</span')

    try:
        xs=128
        tx=0
        revert(ser)

    except KeyboardInterrupt:  # Press Ctrl + C to exit
        print 'Exit'

    ser.close()
