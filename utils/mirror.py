import logging
import json
import re

#  class for mirror
class Mirror(object):

    #  direction
    direction = str()

    # which side is reflective
    rightSide = bool()
    leftSide = bool()


    def __init__(self, direct):
    
        if not direct == "R" and not direct == "L":
            raise Exception("The " + direct + " direction of mirror is not supported.")
        self.direction = direct
        self.rightSide = True
        self.leftSide = True

    def __init___0(self, direct, side):

        self.__init__(direct)
        if not side == "R" and not side == "L":
            raise Exception("The " + side + " of a mirror is not supported.")
        if side == "R":
            self.leftSide = False
        if side == "L":
            self.rightSide = False