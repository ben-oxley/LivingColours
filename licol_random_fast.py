import time
import serial
import random

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

# Loop forever
while 1 :
	# Monitor the serial connection
	if not (ser.isOpen()):
		print "The connection to the device was closed"
		exit(1)

	r=random.randint(1, 255)
	b=random.randint(1, 255)
	g=random.randint(1, 255)


	# Construct the string
	string = 'w0-' + "%03d" % r
	string += '-' + "%03d" % g
	string += '-' + "%03d" % b
	print "Sending command: " + string


	# Append a carriage return and newline
	string += '\r\n'

	# Write the string to the serial port
	ser.write(string)
	time.sleep(0.1)
"""
	# Increment values and handle variable overflow
	r += 1
	b += 1
	g += 1
	if b>254:b=1
	if g>254:g=1
	if r>254:r=1
"""

	# Wait a little bit
