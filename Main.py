# !/usr/bin/python
# -*- coding: utf-8 -*-
from settings import *
from Maps import * 
from CustomExceptions import * 
from utils import *
from classes import *



if __name__ == "__main__":
    mainMap = NodeMap
    car = Car([0,19])
    AgentList = []
    AgentList.append(car)
    for a in AgentList:
        a.run()
