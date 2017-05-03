# !/usr/bin/python
# -*- coding: utf-8 -*-
from settings import * 
from CustomExceptions import *

class Cars(object):

    def __init__(self, position,destination=settings.DEFAULT_DESTINATION,worldMap=WORLDMAP):
        #speed: Return the speed the car is currently at
        self.speed = 0
        #position: Position of the car - ie: the patch it's on
        self.position = position
        #turn_signal_status: Return the status of it's turn signal
        self.turn_signal_status = TURN_SIG_OFF
        #destination: Describes the patch the car wants to go to 
        self.destination = destination
        #current orientation: describes which way the car is oriented
        self.current_orientation = [1,0]



    #ACTUATORS
    def drive(self,orientation=self.current_orientation):
		#Orientation should be something like
        new_pos = [self.position[0] + orientation[0] * self.speed, self.position[1] + orientation[1] * self.speed]
        
        if not possiblePosition(new_pos):
            raise PositionError("I am a car and I'm attempting to drive to impossible position {}".format(new_pos))
        else:
            self.position = new_pos
            checkForCrash(new_pos,world_map)
            return self.position
    
    
    def turnLeft(self):
        """turns the car to the left acording to his perspective, assume a birdseye view!
            effectively [x,y] becomes [-y,x]
        """
        if self.current_orientation not in ACCEPTABLE_ORIENTATIONS:
            raise OrientationError("I am a car and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
        else:
            new_orientation = [  - self.current_orientation [1] , self.current_orientation[0] ]
            return True
            
    def turnRight(self):
        """turns the car to the right acording to his perspective, assume a birdseye view!
            effectively [x,y] becomes [y,-x]
        """
        if self.current_orientation not in ACCEPTABLE_ORIENTATIONS:
            raise OrientationError("I am a car and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
        else:
            new_orientation = [ self.current_orientation [1] ,  - self.current_orientation[0] ]
            return True
        
    def stop(self):
        while self.speed > 0:		 
            hitTheBreaks(self)   
    
    def hitTheBreaks(self):
        new_orientation = [ - self.current_orientation[0] , - self.current_orientation[1] ] 
        self.speed = self.speed - 1
        pos = drive(new_orientation)
        checkForCrash(pos,world_map) 
    def accelerate(self):
        self.speed = self.speed + 1
        drive(self)
    
    #Sensors   
    
