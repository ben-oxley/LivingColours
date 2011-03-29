import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/tty.usbmodem411',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)

ser.open()
ser.isOpen()


input=1
r=1
b=1
g=1
while 1 :
		r.zfill(3)
		g.zfill(3)
		b.zfill(3)
		string = 'w'+str(r)+'-'+str(g)+'-'+str(b)+'\r\n'
		ser.write(string)
		r += 1
		b += 1
		g += 1
		if b>254:b=1
		if g>254:g=1
		if r>254:r=1
		time.sleep(1)
		print string
			


