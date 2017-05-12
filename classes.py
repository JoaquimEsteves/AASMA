# !/usr/bin/python
# -*- coding: utf-8 -*-
from settings import * 
from CustomExceptions import *
from utils import *
from Maps import *



class Car(object):

    def __init__(self, position,destination=DEFAULT_DESTINATION):
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
        self.crashed = False
        self.plan = []
        self.worldmap = WORLDMAP
        #self.checkForCrash = False

    #Sensors   
    #FIX ME

    #ACTUATORS
    def drive(self,orientation=None):
        #Orientation should be something like
        if orientation == None:
            orientation = self.current_orientation
        new_pos = [self.position[0] + orientation[0] * self.speed, self.position[1] + orientation[1] * self.speed]
        if not Node.possiblePosition(new_pos):
            raise PositionError("I am a car and I'm attempting to drive to impossible position {}".format(new_pos))
        else:
            self.position = new_pos
            #abstraction these still don't exist yet
            self.crashed = Node.checkForCrashNode(new_pos, self.worldmap)
            return self.position
    
    
    def turnLeft(self):
        """turns the car to the left acording to his perspective, assume a birdseye view!
            effectively [x,y] becomes [-y,x]
        """
        if self.current_orientation not in ACCEPTABLE_ORIENTATIONS:
            raise OrientationError("I am a car and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
        if self.speed > 2:
            raise CannotTurnError("I am a car that's going a bit too fast to turn!")
        else:
            new_orientation = [  - self.current_orientation [1] , self.current_orientation[0] ]
            return True
            
    def turnRight(self):
        """turns the car to the right acording to his perspective, assume a birdseye view!
            effectively [x,y] becomes [y,-x]
        """
        
        if self.current_orientation not in ACCEPTABLE_ORIENTATIONS:
            raise OrientationError("I am a car and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
        if self.speed > 2:
            raise CannotTurnError("I am a car that's going a bit too fast to turn!")
        else:
            new_orientation = [ self.current_orientation [1] ,  - self.current_orientation[0] ]
            return True
        
    def stop(self):
        while self.speed > 0:		 
            #still doesnt exist
            self.hitTheBreaks(self)
    
    def hitTheBreaks(self):
        new_orientation = [ - self.current_orientation[0] , - self.current_orientation[1] ] 
        self.speed = self.speed - 1
        pos = self.drive(new_orientation)
        #still doesnt existFIXME
        self.crashed =  Node.checkForCrash(pos, self.worldmap)
    def accelerate(self):
        self.speed = self.speed + 1
        self.drive()
    
    def executeNextAction(self,nextAction):
        if nextAction == "accelerate":
            self.accelerate()
        elif nextAction == "hitTheBreaks":
            self.hitTheBreaks()
        elif nextAction == "stop":
            self.stop()
        elif nextAction == "turnRight":
            self.turnRight()
        elif nextAction == "turnLeft":
            self.turnLeft()
        elif nextAction == "drive":
            self.drive()
    #INTELIGENT PARTS    
    #planning
    def planAhead(self):
        return None #FIX ME
    #run cycle
    def run(self):
        #still doesnt existFIXME
        self.crashed = Node.checkForCrash(self.position, self.worldmap)
        if self.crashed == True:
            print "I HAVE CRASHED! THIS IS TERRIBLE!"
            return
        if self.position == self.destination:
            print "I HAVE REACHER MY DESTINATION! {}".format(self.position)
            return
        self.plan = self.planAhead()
        nextAction = self.plan[0]
        for pl in self.plan[:3]:
            if pl.startswith("TURN"):
                #Will be either left or right
                self.turn_signal_status = pl[5:]
                self.executeNextAction(nextAction)
                #we return here just so that we put the turn signal in the currect position
                #imagine for example that we have a plan with turn left drive, then turn right.
                #We want the turn signal to be left, until it turning left is no longer in the first 3 positions of the array
                return
        self.turn_signal_status = TURN_SIG_OFF
        self.executeNextAction(nextAction)
    
class Pedestrian(object):
        def __init__(self, position,destination=DEFAULT_DESTINATION,worldMap=WORLDMAP):
            #speed: Return the speed the car is currently at
            #position: Position of the car - ie: the patch it's on
            self.position = position
            #destination: Describes the patch the car wants to go to 
            self.destination = destination
            #current orientation: describes which way the car is oriented
            self.current_orientation = [1,0]
            self.crashed = False
        
        #sensors FIX ME
        #actuators
        def walk(self,orientation=None):
            #Orientation should be something like
            if orientation == None:
                orientation = self.current_orientation

            new_pos = [self.position[0] + orientation[0] * self.speed, self.position[1] + orientation[1] * self.speed]

            if not Node.possiblePosition(new_pos):
                raise PositionError("I am a person and I'm attempting to walk to impossible position {}".format(new_pos))
            else:
                self.position = new_pos
                #still doesnt exist
                self.crashed = self.checkForCrash(new_pos, self.world_map)
                return self.position
    
    
        def turnLeft(self):
            """turns the car to the left acording to his perspective, assume a birdseye view!
                effectively [x,y] becomes [-y,x]
            """
            if self.current_orientation not in ACCEPTABLE_ORIENTATIONS:
                raise OrientationError("I am a person and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
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
            self.speed = 0
        def accelerate(self):
            self.speed = self.speed + 1
