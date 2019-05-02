#Define the pin to read
pirPin = 13

#Set up the GPIO pin as an input(the pi will listen to the pin for a High/Low state)
GPIO.setmode(GPIO.BCM
GPIO.setup(pirPin, GPIO.IN)

if GPIO.input(pirPin)
