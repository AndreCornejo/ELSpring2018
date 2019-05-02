#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sys
import sqlite3 as db

#Assign GPIO pins
tempPin = 17

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
	else:
		print('Error Reading Sensor')

	return tempFahr

con = db.connect('../log/templog.db')
cur = con.cursor()


#Use the blinkonce function in a loopity-loop when the button is pressed
try:
	while True:
			data = readF(tempPin)
			print ('The Temperature is '+data+ '*F')
			#log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(data1)))
			query = "INSERT INTO templog(date, temp) VALUES('{}', '{}');"
			query = query.format(time.strftime("%Y-%m-%d %H:%M:%S"), data)
			cur.execute(query)
			con.commit()
			os.system('clear')
			print('Date      Temperature')
			for row in cur.execute('SELECT * FROM templog;'):
				print("{}, {}".format(row[0], row[1]))
			time.sleep(60)

except KeyboardInterrupt:
#	os.system('clear')
	print('Thanks for Blinking and Thinking!')
GPIO.cleanup()
