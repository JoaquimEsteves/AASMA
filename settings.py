# !/usr/bin/python
# -*- coding: utf-8 -*-
"""All project settings are defined here"""
import os
# Set loggin as debug level
DEBUG = True

#Constants
DEFAULT_DESTINATION = 'FIX ME'
TURN_SIG_OFF = "OFF"
TURN_SIG_LEFT = "LEFT"
TURN_SIG_OFF = "RIGHT"
DESTINATIONS_REACHED = 0
DESTINATIONS_REACHED_CARS = 0
DESTINATIONS_REACHED_PEDESTRIANS = 0

ACCEPTABLE_ORIENTATIONS = [ [0,1] , [0,-1] , [ 1, 0] [-1,0] ]

#MAP
WORLDMAP = None
