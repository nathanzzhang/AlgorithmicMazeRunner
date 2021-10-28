# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:20:59 2020

@author: Nathan Zhang
@author: Jackie Piepkorn
"""
from motors import Motor
from sensors import UltrasonicRangeFinder
import time

leftSensor = UltrasonicRangeFinder("PartNumber", 'LEFT', 20, 21)
rightSensor = UltrasonicRangeFinder("PartNumber", 'RIGHT', 12, 16)
frontSensor = UltrasonicRangeFinder("PartNumber", 'FRONT', 19, 26)
leftMotor = Motor(18, 23, 3.5)
rightMotor = Motor(4, 17, 3.5)

def main():
    #testStartup()
    stopAllMotors()
    while True:
        leftBlocked = leftSensor.isBlocked()
        rightBlocked = rightSensor.isBlocked()
        frontBlocked = frontSensor.isFrontBlocked()
        step(leftBlocked, rightBlocked, frontBlocked)
    
def testStartup():
    print("Starting left motor forward")
    leftMotor.startPin2()
    time.sleep(1)
    print("Stopping left motor.")
    leftMotor.stop()
    
    print("Starting left motor backward")
    leftMotor.startPin1()
    time.sleep(1)
    print("Stopping left motor.")
    leftMotor.stop()
    
    print("Starting right motor forward")
    rightMotor.startPin1()
    time.sleep(1)
    print("Stopping right motor.")
    rightMotor.stop()
    
    print("Starting right motor backward")
    rightMotor.startPin2()
    time.sleep(1)
    print("Stopping right motor.")
    rightMotor.stop()
    
    print("Left Sensor Distance: " + str(leftSensor.getDistance()))
    print("Right Sensor Distance: " + str(rightSensor.getDistance()))
    print("Front Sensor Distance: " + str(frontSensor.getDistance()))
    time.sleep(1)
    print("All systems checked...proceeding with algorithm...")
    
def step(leftBlocked, rightBlocked, frontBlocked):
    if leftBlocked:
        print('Left too close, adjusting Right. Left distance: ' + str(leftSensor.getDistance()))
        adjustRight()        
    elif rightBlocked:
        print('Right too close, adjusting Left. Right distance: ' + str(rightSensor.getDistance()))
        adjustLeft()       
    time.sleep(0.25)
    if not frontBlocked:
        print("Front clear, moving forward. Front Distance: " + str(frontSensor.getDistance()))
        moveForward()
    else:
        print("Front Blocked, sensing left and right sides")
        stopAllMotors()
        time.sleep(0.2)
        tempRight = rightSensor.getDistance()
        tempLeft = leftSensor.getDistance()
        if tempRight >= tempLeft:
            print("Turning Right")    
            turnRight()
        elif tempLeft > tempRight:
            print("Turning Left")
            turnLeft()
        time.sleep(0.25)
                
def adjustLeft():
    leftMotor.startPin2()
    time.sleep(0.05)
    stopAllMotors()
    
def turnLeft():
    leftMotor.startPin2()
    time.sleep(0.37)
    stopAllMotors()
    
def adjustRight():
    rightMotor.startPin1()
    time.sleep(0.05)
    stopAllMotors()

def turnRight():
    rightMotor.startPin1()
    time.sleep(0.37)
    stopAllMotors()   
    
def moveForward():
    leftMotor.startPin2()
    rightMotor.startPin1()
    time.sleep(0.1)
    stopAllMotors()
    time.sleep(0.25)
    
def moveBackward():
    leftMotor.startPin1()
    rightMotor.startPin2()
    time.sleep(0.1)
    stopAllMotors()
    time.sleep(0.25)

            
def stopAllMotors():
    leftMotor.stop()
    rightMotor.stop()    

if __name__ == '__main__':
    try: 
        main()        
    except KeyboardInterrupt:
        stopAllMotors()
        print("\n--Process terminated by User--")
        
