#!/usr/bin/python3
"""
Jon Friedman
FRDJON009
Prac1
29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
c = 16
# Logic that you write
def main():
	init_GPIO()
	while(True):
		pass

#initiate GPIO pins as inputs and outputs
def init_GPIO():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(27, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(6, GPIO.FALLING, bouncetime = 300)
	GPIO.add_event_callback(6, callback=callback1)
	GPIO.add_event_detect(16, GPIO.FALLING, bouncetime = 300)
	GPIO.add_event_callback(16, callback=callback2)
#check the bits of the counter and update led display
def LED():
	global c
	if (c==0):
		c = 8 
	if(c & 1):
		GPIO.output(26, GPIO.HIGH)
	else:
		GPIO.output(26, GPIO.LOW)
	if(c & 2):
		GPIO.output(17, GPIO.HIGH)
	else:
		GPIO.output(17, GPIO.LOW)
	if(c & 4):
		GPIO.output(27, GPIO.HIGH)
	else:
		GPIO.output(27, GPIO.LOW)
#interupt used to inrement counter
def callback1(channel):
	global c
	c = c+1
	LED()
#interupt used to decrease counter
def callback2(channel):
	GPIO.output(27, GPIO.HIGH)
	global c
	if(c>0):
		c = c - 1  
	LED()
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
