#!/usr/bin/sudo /usr/bin/python
#usage ./name 17 18 22 23 (LSD to MSD)

import RPi.GPIO as GPIO
import time
import sys

def timedOn(gpio, duration):
   print "sleep %f gpio %d" % (duration, gpio)
   
   #set mode
   GPIO.setmode(GPIO.BCM)
   
   #setup gpios
   GPIO.setup(gpio, GPIO.OUT)
   
   # timed exposure
   GPIO.output(gpio,1)
   time.sleep(duration)
   GPIO.output(gpio,0)

def main():
   gpio=int(sys.argv[1])
   duration=float(sys.argv[2])
   
   timedOn(gpio,duration)

if __name__ == "__main__":
   main()
