# !/usr/bin/python
# -*- coding: utf-8 -*-
from settings import * 
from CustomExceptions import *
from utils import *
from Maps import *

#log = Logger(debug=settings.DEBUG)

class Agent(object):
    def __init__(self,id,position,orientation=[1,0],destination=DEFAULT_DESTINATION,map=NodeMap):
        self._id = id
        self._worldmap = map
        #position: Position of the car - ie: the patch it's on
        self.position = position
        #destination: Describes the patch the agent wants to go to
        self.destination = destination
        self._orientation = orientation
        self._speed = 0
        self._reachedDestination = False
        
    def __eq__(self, other):
        """two agents are equal if they have the same id
        we are overriding pythons == method, similarly to java's .equals()"""
        return self._id == other._id
    
    def addSelfToNewNode(self,x,y):
        self._worldmap[x][y]._ocupiedBy.append(self)
        
    def move(self):
        print "If you see this message I have an object oriented error!"


        
class Car(Agent):

    def __init__(self,id, position,orientation=[1,0],destination=DEFAULT_DESTINATION):
        #visual representation to be used in the map!
        Agent.__init__(self,id,position,orientation,destination)
        self._visual = 'C'
        self._id = id
        #turn_signal_status: Return the status of it's turn signal
        self._turn_signal_status = TURN_SIG_OFF
        self._crashed = False
        #dijsktra
        self._plan = self.planAhead()
        for i in self._plan:
            print i._position
    #Sensors   
    #FIX ME
    #zebra ahead?
    
    def getCurrentNode(self):
        """return current node on the world map"""
        return self._worldmap[self.position[0]][self.position[1]]
 
    #Check if I changed orientation!
    def setOrientation(self,oldNode,newNode):
        """check if I'm going to have to change orientation to go from the old node to the new one!"""
        if self._speed == 0 or (oldNode._position == newNode._position) :
            return False
        if newNode._position != ( oldNode._position[0] + self._orientation[0] , oldNode._position[1] + self._orientation[1]):
            turn_left = [  - self._orientation [1] , self._orientation[0] ]
            turn_right = [ self._orientation [1] ,  - self._orientation[0] ]
            
            #log.debug("I HAVE TO CHANGE MY ORIENTATION!")
            
            if newNode._position == ( oldNode._position[0] + turn_left[0], oldNode._position[1] + turn_left[1]):
                #log.debug("I HAVE TURNED LEFT!")
                self._orientation = turn_left
                return TURN_SIG_LEFT
            elif newNode._position == ( oldNode._position[0] + turn_right[0], oldNode._position[1] + turn_right[1]):
                #log.debug("I HAVE TURNED RIGHT!")
                self._orientation = turn_right
                return TURN_SIG_RIGHT
            else:
                #log.error("THIS PLAN IS TELLING ME TO GO BACKWARDS!")
                print "THIS PLAN IS TELLING ME TO GO BACKWARDS!"
                print newNode._position
                print oldNode._position
                print self._orientation
                print turn_right
                print turn_left
                raise OrientationError()
                
    def dangerAhead(self):
        """Main planning function, tells us if we are free to accelerate, if we can just stay at the same speed or if we have to break!"""
        #visible_zone = [[None for x in range(10)] for y in range(10)]
        nearby_objects = []
        
        for line in range(max(self.position[0] - 5,0), min(self.position[0] + 6,19)): 
            for column in range(max(self.position[1] - 5,0), min(self.position[1] + 6,39)):
                if self._worldmap[line][column]._ocupiedBy != []:
                    nearby_objects += [self._worldmap[line][column]._ocupiedBy[0]]
        my_orientation = self._orientation
        for obj in nearby_objects:
            obj_orientation = obj._orientation
            obj_position = obj.position
            obj_speed = obj._speed
            other_positions = []
            for v in range(obj_speed):
                other_positions += [(v+1)*obj_orientation[0], (v+1)*obj_orientation[1]]
            for other_pos in other_positions:
                for my_pos in self._plan:
                    if other_pos == my_pos._position:
                        return True
        return False

    #ACTUATORS
    def drive(self):
        """function that moves the car. If speed is 0 goes nowhere.
        slowing down and accelerating still call this function"""
        #this will be my final position, based on my speed!
        if self.position == self.destination:
            print "I HAVE REACHER MY DESTINATION! {}".format(self.position)
            self._reachedDestination = True
        if self._speed != 0 and len(self._plan) > 1:
            final_node = self._plan[1]
            previous_node = self.getCurrentNode()
            self.getCurrentNode().removeFromOcupied(self)
            #So now for every node I'm going to drive through, I have to check if I'll crash into something!
            
            #remove this node form the plan since i'm going to drive away from it!
            
            
            self._plan = self._plan[1:]
            
            self._plan[0]._ocupiedBy.append(self)
            self.setOrientation(previous_node,self._plan[0])
            if self._plan[0].checkForCrashNode():
                self.crashed = True
                print "I HAVE CRASHED!"
                #log.info("I am a car and I've crashed at position {} {} !".format(self.position[0],self.position[1]))

            self.position = final_node._position
            self.addSelfToNewNode(self.position[0],self.position[1])
            return self.position
    
    def move(self):
        """Overriding super class method"""
        self.drive()
    
    def stop(self):
        while self.speed > 0:		 
            #still doesnt exist
            self.hitTheBreaks(self)
    
    def hitTheBreaks(self):
        self.speed = self.speed - 1
        #pos = self.drive()
        #self.crashed =  self.getCurrentNode().checkForCrash()
    
    def accelerate(self):
        self._speed = self._speed + 1
        #self.drive()
    
    # def executeNextAction(self,nextAction):
        # if nextAction == "accelerate":
            # self.accelerate()
        # elif nextAction == "hitTheBreaks":
            # self.hitTheBreaks()
        # elif nextAction == "stop":
            # self.stop()
        # elif nextAction == "turnRight":
            # self.turnRight()
        # elif nextAction == "turnLeft":
            # self.turnLeft()
        # elif nextAction == "drive":
            # self.drive()
    ##################INTELIGENT PARTS################################################################    
    #planning
    def planAhead(self):
        """applies disjktras algorithm"""
        #hashable_position =
        return shortest_path(CAR_GRAPH, self._worldmap[self.position[0]][self.position[1]],  self._worldmap[self.destination[0]][self.destination[1]])
    
    #actiave turn signals, or not!
    def checkForTurns(self):
        """sets the value of turn signal to left or right if the car is going to turn soon
            how soon depends on it's speed!
        """
        currentNode = self.getCurrentNode()
        try: 
            for nextNode in self._plan[:self._speed]:
                if self.setOrientation(currentNode, nextNode):
                    self._turn_signal_status = self.setOrientation(currentNode, nextNode)
                    return
            self._turn_signal_status = TURN_SIG_OFF
        except:
            #only happens if speed is 0
            pass
    
    #run cycle
    def run(self):
        """The run function determines whether the car will simply drive, accelerate or brake!"""
        if self._crashed == True:
            print "I HAVE CRASHED! THIS IS TERRIBLE!"
            return
        if self.position == self.destination:
            print "I HAVE REACHER MY DESTINATION! {}".format(self.position)
            return

        #This function returns left right or no turn signal depending on if there is a turn coming up soon.
        self.turn_signal_status = self.checkForTurns() 
        
        #Plan next action
        if self.dangerAhead():
            self.hitTheBreaks()
        else:
            self.accelerate()
            
        speed_to_return = self._speed
        return [self,speed_to_return]

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


