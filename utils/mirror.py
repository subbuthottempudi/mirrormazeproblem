import logging
import json
import re


#  direction
direction = str()

# which side is reflective
rightSide = bool()
leftSide = bool()


def twomirror(direct):

    if not direct == "R" and not direct == "L":
        raise Exception("The " + direct + " direction of mirror is not supported.")
    direction = direct
    rightSide = True
    leftSide = True

def onemirror(direct, side):
    if not side == "R" and not side == "L":
        raise Exception("The " + side + " of a mirror is not supported.")
    if side == "R":
        leftSide = False
    if side == "L":
        rightSide = False