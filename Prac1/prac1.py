#!/usr/bin/python3
"""
Jon Friedman
FRDJON009
Prac1
29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    init_GPIO()



def init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT)
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	GPIO.add_event_detect(6, GPIO.RISING, bouncetime = 300)
	GPIO.add_event_callback(6, callback=callback1())
	GPIO.add_event_detect(16, GPIO.RISING, bouncetime = 300)
	GPIO.add_event_callback(16, callback=callback2())


def callback1(channel):
	GPIO.output(18,GPIO.HIGH)

def callback2():
	GPIO.output(17, GPIO.HIGH)

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
