#usage ./name 17 18 22 23 (LSD to MSD)

import RPi.GPIO as GPIO
import time
import sys

gpios=[ int(num) for num in sys.argv[1:] ]
numbits=len(gpios)

def displayNumber(number):
   for i in range(0, numbits):
      GPIO.output(gpios[i], number >> i & 0x1 == 1)

#set mode
GPIO.setmode(GPIO.BCM)

#setup gpios
for gp in gpios:
   GPIO.setup(gp, GPIO.OUT)

# basic counting:
print "showcasing a %s-bit counter" % numbits
while True:
   for i in range(0, 2**numbits):
      displayNumber(i)
      time.sleep(1)


