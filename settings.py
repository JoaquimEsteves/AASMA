# !/usr/bin/python
# -*- coding: utf-8 -*-
"""All project settings are defined here"""
import os
# Set loggin as debug level
DEBUG = True

#Constants
DEFAULT_DESTINATION = 'FIX ME'
TURN_SIG_OFF = 0
TURN_SIG_LEFT = 1
TURN_SIG_OFF = 2

ACCEPTABLE_ORIENTATIONS = [ [0,1] , [0,-1] , [ 1, 0] [-1,0] ]

#MAP
WORLDMAP = None
