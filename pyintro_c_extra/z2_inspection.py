'''
@summary: Python Intro - Naming rules
'''
__author__ = 'patrick'

class Vehicle(object):
    def __init__(self, name):
        """ Constructor """
        self.name = name

    def move(self, distance =1):
        """
        :param distance: how far?
        :return: true/false if the move was successful
        """
        pass

#dir command
print (dir(Vehicle))

# pprint
from pprint import pprint
pprint (dir(Vehicle))

# help
help(Vehicle)
help(Vehicle.move)

# help build in
import os
#help(os)
#help(os.walk)