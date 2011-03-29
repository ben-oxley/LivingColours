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

	r1=random.randint(-3, 3)
	b1=random.randint(-3, 3)
	g1=random.randint(-3, 3)
	r=r-r1
	b=b-b1
	g=g-g1

	# Construct the string
	string = 'w0-' + "%03d" % r
	string += '-' + "%03d" % g
	string += '-' + "%03d" % b
	print "Sending command: " + string


	# Append a carriage return and newline
	string += '\r\n'

	# Write the string to the serial port
	ser.write(string)
	time.sleep(0.05)

	# Increment values and handle variable overflow
	# r += 1
	# b += 1
	# g += 1
	if b>254:b=128
	if g>254:g=128
	if r>254:r=128


	# Wait a little bit
