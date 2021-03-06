# !/usr/bin/python
# -*- coding: utf-8 -*-
"""All project settings are defined here"""
import os
from Maps import *
# Set loggin as debug level
DEBUG = True

#Constants
DEFAULT_DESTINATION = [11,1]
TURN_SIG_OFF = "OFF"
TURN_SIG_LEFT = "LEFT"
TURN_SIG_RIGHT = "RIGHT"
DESTINATIONS_REACHED = 0
DESTINATIONS_REACHED_CARS = 0
DESTINATIONS_REACHED_PEDESTRIANS = 0


WALL = 'X'
FREE = ' '
PARKING_SPOT = 'E'
ZEBRA = 'Z'
PEDESTRIAN_ZONE = '0'


ACCEPTABLE_ORIENTATIONS = [ [0,1], [0,-1], [1, 0], [-1,0] ]

#MAP
WORLDMAP = NodeMap #comes from Maps




