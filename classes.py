# !/usr/bin/python
# -*- coding: utf-8 -*-
from settings import * 
from CustomExceptions import *
from utils import *
from Maps import *

log = Logger(debug=settings.DEBUG)

class Agent(object):
    def __init__(self,id,position,destination=DEFAULT_DESTINATION):
        self._id = id
        self._worldmap = WORLDMAP
        #position: Position of the car - ie: the patch it's on
        self.position = position
        #destination: Describes the patch the agent wants to go to
        self.destination = destination
        
    def __eq__(self, other):
        return self._id == other._id
    
    def addSelfToNewNode(self,x,y):
        self._worldmap[x][y]._ocupiedBy.append(self)
        
        
        
class Car(Agent):

    def __init__(self,id, position,destination=DEFAULT_DESTINATION):
		#visual representation to be used in the map!
        Agent.__init__(self,id,position,destination)
        self._visual = 'C'
        self._id = id
        #speed: Return the speed the car is currently at
        self._speed = 0
        #turn_signal_status: Return the status of it's turn signal
        self._turn_signal_status = TURN_SIG_OFF
        self._crashed = False
        #dijsktra
        self._plan = self.planAhead()
    
        #self.checkForCrash = False

    #Sensors   
    #FIX ME
    #zebra ahead?
       
    def getCurrentNode(self):
        return self._worldmap[self._position[0]][self._position[1]]
    
    def check_zebra(self):
        #how many nodes ahead
        if self.position == ZEBRA:
            self.hitTheBreaks()
        elif self.position == ZEBRA and self.position == Pedestrian:
            self.stop()
    #parking lot?
    #road ahead?
    #if we want to make things harder check for people 2 or 3 nodes ahead


    #ACTUATORS
    def drive(self):
        #this will be my final position, based on my speed!
        final_node = self._plan[self._speed]
        self.getCurrentNode().removeFromOcupied(self)
        #So now for every node I'm going to drive through, I have to check if I'll crash into something!
        for i in self._plan[self._speed]:
            i._ocupiedBy.append(self)
            if i.checkForCrashNode():
                self._crashed = True
                log.info("I am a car and I've crashed at position {} {} !".format(self._position[0],self._position[1])
            else:
                i.removeFromOcupied(self)
        
        self._position = final_node._position
        return self._position
            
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
    ###################INTELIGENT PARTS################################################################    
    #planning
    def planAhead(self):
        return None #FIX ME
        
    #run cycle
    def run(self,MAP):
        if self.crashed == True:
            print "I HAVE CRASHED! THIS IS TERRIBLE!"
            return
        if self.position == self.destination:
            print "I HAVE REACHER MY DESTINATION! {}".format(self.position)
            return
        
        #This function returns left right or no turn signal depending on if there is a turn coming up soon.
        self.turn_signal_status = self.checkForTurns() #FIX ME TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        #Plan next action
        if self.dangerAhead():#FIX ME
            self.hitTheBreaks() 
            log.info("I (id:{}) am going to slow down a bit! My speed is {}".format(self._id,self._speed))
            return
        
        if self.allClearAhead() #FIX ME
            self.accelerate()
            log.info("HAHA I THE FEARLESS (id:{}) AM GOING TO ACCELERATE MY BOYS!".format(self._id,self._speed))
            return
            
        self.drive()
        log.info("I (id:{}) am just going to keep driving at this pace! {}".format(self._id,self._speed))
    
class Pedestrian(Agent):
        def __init__(self,id, position,destination=DEFAULT_DESTINATION):
            Agent.__init__(self,id,position,destination)
            
            #visual representation to be used in the map
            self._visual = 'P'
            #current orientation: describes which way the car is oriented
            self.current_orientation = [1,0]
            self.crashed = False
        
        #sensors FIX ME

        #should be check for car in the 2 or 3 nodes on the left/right?
        #if zebra
        #if road
        #if parking lot?
        #thats it i guess
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