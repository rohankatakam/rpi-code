#import Libraries
import RPi.GPIO as GPIO
import time
import pyrebase

#Firebase Configuration
config = {
  "apiKey": "apiKey",
  "authDomain": "testproject-f514d.firebaseapp.com",
  "databaseURL": "https://testproject-f514d.firebaseio.com",
  "storageBucket": "testproject-f514d.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

#Firebase Database Intialization
db = firebase.database()

#While loop to run until user kills program
while(True):
    #Get value of LED 
    led = db.child("led").get()

    #Sort through children of LED(we only have one)
    for user in led.each():
        #Check value of child(which is 'state')
        if(user.val() == "OFF"):
            #If value is off, turn LED off
            GPIO.output(18, False)
        else:
            #If value is not off(implies it's on), turn LED on
            GPIO.output(18, True)

        #0.1 Second Delay
        time.sleep(0.1)   

