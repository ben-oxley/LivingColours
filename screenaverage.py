import time
import serial
import random
from PIL import Image
import os

class PixelCounter(object):
  ''' loop through each pixel and average rgb '''
  def __init__(self, imageName):
      self.pic = Image.open(imageName)
      # load image data
      self.imgData = self.pic.load()
  def averagePixels(self):
      r, g, b = 0, 0, 0
      count = 0
      #xval=xrange(self.pic.size[0])
      #xcoun=xval/100
      #yval=xrange(self.pic.size[1])
      #ycoun=yval/100
      xval=self.pic.size[0]
      xcoun=xval/100
      yval=self.pic.size[1]
      ycoun=yval/100
      for x in range(1,xcoun):
          for y in range(1,ycoun):
	      ydist=y*100
	      xdist=x*100
              tempr,tempg,tempb = self.imgData[xdist,ydist]
              r += tempr
              g += tempg
              b += tempb
              count += 1
      # calculate averages
      return (r/count), (g/count), (b/count), count


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/tty.usbmodem411',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

ser.open()

# Check we opened the port correctly
if not (ser.isOpen()):
	print "Failed to open the serial port"
	exit(1)

# Initialise all variables
input=1
r=128
b=128
g=128
r_last=0
b_last=0
g_last=0
r_diff=0
b_diff=0
g_diff=0

# Loop forever
while 1 :
	# Monitor the serial connection
	if not (ser.isOpen()):
		print "The connection to the device was closed"
		exit(1)

	os.system("screencapture 1.jpg")
  	pc = PixelCounter('1.jpg')
	r, g, b, count = pc.averagePixels()
	r_diff= r - r_last
	b_diff= b - b_last
	g_diff= g - g_last
	for i in range(1,10):
		r_out = r - (r_diff/i)
		g_out = g - (g_diff/i)
		b_out = b - (b_diff/i)
		# Construct the string
		string = 'w0-' + "%03d" % r_out
		string += '-' + "%03d" % g_out
		string += '-' + "%03d" % b_out
		print "Sending command: " + string

	
		# Append a carriage return and newline
		string += '\r\n'

		# Write the string to the serial port
		ser.write(string)
		time.sleep(0.01)


	r_last=r
	g_last=g
	b_last=b

	# Wait a little bit
	time.sleep(0.01)
