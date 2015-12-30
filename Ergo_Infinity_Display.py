	#!/usr/bin/env python

	# Author: Ilia Baranov

import serial
from timeit import timeit
from time import sleep
from math import floor

# Fonts created for ease of Use
from Fonts import *

lcd = [[0 for x in range(32)] for x in range(128)] 

#LCD is arranged with 0,0 at lower left corner
# first [] is x direct, second [] is y

lcd[0][0]=1
lcd[2][0]=1 # Test pattern to ensure orientation
lcd[0][2]=1

# Fairly painless way to do fonts		
def send_char(array,c,x,y): #Enter a char at location x,y using small 5x8 font
	for w in range (5):	
		#if (x+w <= len(array)) & (y+8 <= len(array[0])): #Boundrary checking
		array[x+w][y:y+8] = list(format(QuickType_5x8[(ord(c)-32)*5+w], '08b'))
		
def send_string(array,str,x,y):
	for i, c in enumerate (str):
		send_char(array,c,x+i*5,y)
		
def clear(array,ser): # Clean lcd array and clean screen
	for x in range (len(array)):
		for y in range (len(array[0])):
			array[x][y] = 0
	ser.write("lcdInit \r")
	sleep(0.1)
	
def lcd_color(r,g,b,ser):
	command = "lcdColor " + str(r) + " " + str(g) + " " + str(b) + " \r"
	ser.write(command)
	sleep(0.05)
			
def send(array,ser): #Pass an array, for updating the whole screen, slow!
	for segs in range (8): # have to break into 8 segments of 16 to avoid lcd overload
		for y in range (len(array[0])/8):
			command = "lcdDisp " + hex(y) + " " + hex(segs*16) + " "
			for x in range (len(array)/8):
				val = ""
				for w in range (7,-1,-1):
					val += str(array[x+segs*16][y*8+w])
				command += hex(int(val, 2)) + " "
			command += "\r"
			ser.write(command)
			#print command
			sleep(0.03) #Fastest I can go before artefacts start to appear

def update_pixel(array,x,y,val,ser): #Update a single pixel at location x,y, with either 1 or 0
	array[x][y]= val;
	ypose = int(floor(y/8))
	val = ""
	for w in range (7,-1,-1):
		val += str(array[x][ypose*8+w])
	command = "lcdDisp " + hex(ypose) + " " + hex(x) + " " + hex(int(val, 2)) + " \r"
	ser.write(command)
	#print command
	sleep(0.03)
			
#NOTE: This will update to the upper limit of the Y page stored, as this is actually faster than limiting it to a smaller section
def send_portion(array,xDims,yDims): # Update part of the screen, faster for small updates (~30 pixels total)
	for y in range (yDims[0],yDims[1],2):
		for x in range (xDims[0],xDims[1]):
			update_pixel(array,x,y,array[x][y])


if __name__ == '__main__':		
	ser = serial.Serial(28, 115200, timeout=0.5) #Change to (Serial port - 1) on Windows.
	ser.close()
	ser.open()
	
	for x in range (54,74):
		for y in range (6,26):
			lcd[x][y] = 1
	
	send_char(lcd,'!', 4, 0)
	
	send_string(lcd,"TEST 1,2,3 ", 4, 10)
	send_string(lcd,"", 4, 0)

	
	#This chunk shows time it takes for different operations
	print "\n\rTiming Tests"
	print "Update Full LCD: " + str(timeit("send(lcd,ser)",setup="from __main__ import send,lcd",number=1)) # Send 3 dot test pattern
	print "Clear LCD: " + str(timeit("clear(lcd,ser)",setup="from __main__ import clear,lcd",number=1)) # Clear LCD array, and clear screen
	print "Update 1 individual pixel: " + str(timeit("update_pixel(lcd,1,1,1,ser)",setup="from __main__ import update_pixel,lcd",number=1)) # Send individual pixels, while keeping exisiting data from array

	 # Fill LCD array with block of  checkerboard data
	v = 1
	for x in range (8,20):
		v ^= 1
		for y in range (10,30):
			lcd[x][y] = v
			v ^= 1

	print "Update block of LCD: " + str(timeit("send_portion(lcd,[10,15],[20,25])",setup="from __main__ import send_portion,lcd",number=1)) # Upload smaller portion of data to test speed		


	ser.close()