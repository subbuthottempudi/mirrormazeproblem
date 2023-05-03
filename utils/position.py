#  used to track position in the path
class Position(object):
   
    col = int()
    row = int()
    orientation = str()

    #  "H" or "V"
    direction = str()

    #  "+": increase step; "-": decrease step
    def __init__(self, c, r, o, d):
      
        self.col = c
        self.row = r
        
        if not o == "H" and not o == "V":
            raise Exception("The " + o + " direction of mirror is not supported.")
        self.orientation = o
        if not d == "+" and not d == "-":
            raise Exception("The " + d + " direction of movement is not supported.")
        self.direction = d

    def __str__(self):
       
        return "position: " + self.col + "x" + self.row + " (" + self.orientation + self.direction + ") "

    def equals(self, p):
      
        if self.col == p.col and self.row == p.row and self.orientation == p.orientation and self.direction == p.direction:
            return True
        else:
            return False