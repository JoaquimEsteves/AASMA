# !/usr/bin/python
# -*- coding: utf-8 -*-
from Maps import * 
from CustomExceptions import * 
from settings import *
from utils import *
from classes import *

def moveAgents(listAgents,worldmap = NodeMap):
    move_cycles_list = []
    for agent in listAgents:
        move_cycles_list += [agent.run()]
    while move_cycles_list != []:
        for agnt in move_cycles_list:
            if agnt[1] < 0:
                raise NegativeSpeedError()
            if agnt[1] == 0:
                move_cycles_list.remove(agnt)
            else:
                agnt[0].move()
                if agnt[0]._crashed == True:
                    print "This agent has crashed, he'll be removed from the run cycle and list of agents around!"
                    move_cycles_list.remove(agnt)
                    listAgents.remove(agnt[0])
                if agnt[0]._reachedDestination == True:
                    print "This agent has reached his destination! He'll be removed from the run cycle!"
                    move_cycles_list.remove(agnt)
                    listAgents.remove(agnt[0])
                agnt[1] = agnt[1] - 1
            

if __name__ == "__main__":
    mainMap = NodeMap
    car = Car(1,[0,19])
    AgentList = []
    AgentList.append(car)
    while AgentList != []:
        moveAgents(AgentList,mainMap)
