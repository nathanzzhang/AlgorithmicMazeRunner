# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:15:01 2020

@author: Nathan Zhang
@author: Jackie Piepkorn
"""

import RPi.GPIO as GPIO

class Motor:
    
    def __init__(self, pin1, pin2, radius):
        self.mPin1 = pin1
        self.mPin2 = pin2
        self.mRadius = radius
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mPin1, GPIO.OUT)
        GPIO.setup(self.mPin2, GPIO.OUT)
        
    def setMotorPin1(self, newPin1):
        self.mPin1 = newPin1
        
    def setMotorPin2(self, newPin2):
        self.mPin2 = newPin2
        
    def setRadius(self, newRadius):
        self.mRadius = newRadius
        
    def getMotorPin1(self):
        return self.mPin1
    
    def getMotorPin2(self):
        return self.mPin2
    
    def getRadius(self):
        return self.mRadius
    
    def startPin1(self):
        GPIO.output(self.mPin1, True)
        
    def startPin2(self):
        GPIO.output(self.mPin2, True)
        
    def stop(self):
        GPIO.output(self.mPin1, False)
        GPIO.output(self.mPin2, False)
