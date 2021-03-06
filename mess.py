#!/usr/bin/python

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/serial/by-id/usb-H-Tronc_GmbH_HB627_-_12bit_USB_ADC-if00',
    baudrate=38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.open()
ser.isOpen()

while 1 :
        ser.write(r"c01") # + '\r\n')
        out = ''

        time.sleep(0.1)
	
        while ser.inWaiting() > 0:
            out += ser.read(3)
    
            if out != '':
		print(str(256 * ord(out[0]) + ord(out[1])) +  " mV")
