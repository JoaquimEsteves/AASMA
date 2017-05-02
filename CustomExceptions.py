# !/usr/bin/python
# -*- coding: utf-8 -*-
class PositionError(Exception):
    def __init__(self, message="Something went wrong with the position"):

        # Call the base class constructor with the parameters it needs
        super(PositionError, self).__init__(message)

        # Now for your custom code...
        #self.errors = errors
