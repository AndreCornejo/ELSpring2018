import time
import RPi.GPIO as GPIO
import sqlite3
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
 
while True:
 
    if GPIO.input(23)==True:
        GPIO.output(24,True)
        time.sleep(5)
        GPIO.output(24,False)
        conn=sqlite3.connect('PIRlog.db')
        curs=conn.cursor()
        curs.execute("INSERT INTO pir values(datetime('now'))")
        conn.commit()
        conn.close()
