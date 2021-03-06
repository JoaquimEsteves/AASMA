# !/usr/bin/python
# -*- coding: utf-8 -*-

class NegativeSpeedError(Exception):
    def __init__(self,message="Something went wrong with my speed!"):
        super(NegativeSpeedError,self).__init__(message)

class PositionError(Exception):
    def __init__(self, message="Something went wrong with the position"):

        # Call the base class constructor with the parameters it needs
        super(PositionError, self).__init__(message)

        # Now for your custom code...
        #self.errors = errors

class OrientationError(Exception):
    def __init__(self, message="Something went wrong with the orientation"):

        # Call the base class constructor with the parameters it needs
        (PositionError, self).__init__(message)

        # Now for your custom code...
        #self.errors = errors

class CannotTurnError(Exception):
    def __init__(self, message="Something went wrong with the turning point"):

        # Call the base class constructor with the parameters it needs
        (PositionError, self).__init__(message)

        # Now for your custom code...
        #self.errors = errors