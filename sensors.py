# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:20:36 2020

@author: Nathan Zhang
@author: Jackie Piepkorn
"""
import RPi.GPIO as GPIO
import time

class UltrasonicRangeFinder:
    
    def __init__(self, identification, location, 
                 triggerPin, echoPin):
        # Class UltrasonicRangeFinder takes a ID, 
        # a location, a trigger pin, and
        # an echo pin to create a sensor      
        self.mID = identification        
        self.mLocation = location      
        self.mTriggerPin = triggerPin       
        self.mEchoPin = echoPin     
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mTriggerPin, GPIO.OUT)   
        GPIO.setup(self.mEchoPin, GPIO.IN)
            
    
    # GET methods follow
    def getDistance(self):
        # returns the distance measured by the 
        GPIO.output(self.mTriggerPin, True)
        time.sleep(0.00001)
        GPIO.output(self.mTriggerPin, False)
        startTime = time.time()
        stopTime = time.time()
        while(GPIO.input(self.mEchoPin) == 0):
            startTime = time.time()
        while(GPIO.input(self.mEchoPin) == 1):
            stopTime = time.time()
        timeElapsed = stopTime - startTime
        return (timeElapsed * 34300) / 2
        
    def getID(self):
        # returns the ID number
        return self.mID
    
    def getLocation(self):
        # returns location of the sensor
        return self.mLocation
    
    def getTriggerPin(self):
        return self.mTriggerPin
    
    def getEchoPin(self):
        return self.mEchoPin
    
    
    
    # SET methods follow                
    def setID(self, identification):
        self.mID = identification
            
    def setLocation(self, location):
        self.mLocation = location
        
    def setEchoPin(self, echo):
        self.mEchoPin = echo
        
    def setTriggerPin(self, trigger):
        self.mTriggerPin = trigger
        
    
    
    # Methods
    def isBlocked(self):
        # Will determine if the sensor is blocked. Threshold is 0.1 meters
        if self.getDistance() < 10:
            return True
        else:
            return False

    def isFrontBlocked(self):
        # Will determine if the front sensor is blocked. Threshold is 0.1 meters
        if self.getDistance() < 15:
            return True
        else:
            return False
