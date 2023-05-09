import logging
import json
import re

    
def twomirror(direct):

    # direction
    direction = str()

    # which side is reflective
    rightSide = bool()
    leftSide = bool()

    if not direct == "R" and not direct == "L":
        raise Exception("The " + direct + " direction of mirror is not supported.")
    
    direction = direct
    rightSide = True
    leftSide = True

    return direction, leftSide, rightSide

def onemirror(direct, side):

    # direction
    direction = str()

    # which side is reflective
    rightSide = bool()
    leftSide = bool()

    direction = direct

    if not side == "R" and not side == "L":
        raise Exception("The " + side + " of a mirror is not supported.")
    
    if side == "R":
        leftSide = False
        rightSide = True

    if side == "L":
        rightSide = False
        leftSide = True
        
    return direction, leftSide, rightSide