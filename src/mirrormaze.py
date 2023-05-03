from utils import mirror
from utils import position
import array
import io
import logging

        
def mazePath(cls, board, col, row, orientation):
        
        if col < 0 or row < 0 or col >= board.length or row >= board[0].length or (not orientation == "H" and not orientation == "V"):
            print("incorrect input")
            return
        print ("the demensions of board: " + board.length + " x " + board[0].length)
        path = []
        direction = "+"
        path.add(position.Position(col, row, orientation, direction))
        last = path.get(len(path) - 1)
        while (last.col >= 0 and last.col < board.length) and (last.row >= 0 and last.row < board[0].length):
            nextPosition(board, path)
            last = path.get(len(path) - 1)
        print("the path of the laser: ")

        i = 0
        while i < len(path) - 1:
            print(path)
            i += 1
            
def nextPosition(cls, board, path):
        """ method nextPosition """
        prev = path.get(len(path) - 1)
        prevCol = prev.col
        prevRow = prev.row
        prevOrient = prev.orientation
        prevDirection = prev.direction
        nextCol = -1
        nextRow = -1
        nextOrient = prevOrient
        nextDirection = prevDirection

        if prevOrient == "H":
            nextCol = prevCol + (1 if (prevDirection == "+") else -1)
            nextRow = prevRow

        if prevOrient == "V":
            nextRow = prevRow + (1 if (prevDirection == "+") else -1)
            nextCol = prevCol

        if (nextCol >= 0 and nextCol < board.length) and (nextRow >= 0 and nextRow < board[0].length):
            if mirror != None:
                if mirror.direction == "R":
                    if mirror.rightSide:
                        if prevOrient == "V" and prevDirection == "+":
                            nextOrient = "H"
                            nextDirection = "+"
                        if prevOrient == "H" and prevDirection == "-":
                            nextOrient = "V"
                            nextDirection = "-"
                    if mirror.leftSide:
                        if prevOrient == "V" and prevDirection == "-":
                            nextOrient = "H"
                            nextDirection = "-"
                        if prevOrient == "H" and prevDirection == "+":
                            nextOrient = "V"
                            nextDirection = "+"
                if mirror.direction == "L":
                    if mirror.rightSide:
                        if prevOrient == "V" and prevDirection == "-":
                            nextOrient = "H"
                            nextDirection = "+"
                        if prevOrient == "H" and prevDirection == "-":
                            nextOrient = "V"
                            nextDirection = "+"
                    if mirror.leftSide:
                        if prevOrient == "V" and prevDirection == "+":
                            nextOrient = "H"
                            nextDirection = "-"
                        if prevOrient == "H" and prevDirection == "+":
                            nextOrient = "V"
                            nextDirection = "-"
        next = position.Position(nextCol, nextRow, nextOrient, nextDirection)
        for p in path:
            if p == next:
                raise Exception("the laser is trapped in the maze.")
        path.add(next)

class MirrorMaze(object):
    """ class MirrorMaze """
    def main(cls, args):
        """ method main """

        #Logging configuration
        logging.basicConfig(filename='logs/debug.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.disable(logging.DEBUG)

        if args.length == 0:
            print ("please give input file.")
            logging.info('please give input file ' )
            return
        
        mazeRow = 0
        mazeCol = 0
        mirrors = []
        laserStartRow = -1
        laserStartCol = -1
        laserOrientation = None
        inputCounter = 0

        in_ = open(args[0],'r')
        logging.info('Opening the input file ')
        
        #  read the configuration for the mirror board and the laser
        #  TO-DO: to catch all kinds of input file exceptions.
        while in_.hasNextLine():
            if nextLine.startsWith("-1"):
                inputCounter += 1
                if in_.hasNext():
                    nextLine = in_.nextLine().trim()
            #  read maze size
            if inputCounter == 0:
                mazeSize = nextLine
                mazeCol = int(mazeSize.trim().split(",")[0])
                mazeRow = int(mazeSize.trim().split(",")[1])
            #  read mirror
            if inputCounter == 1:
                mirrors.add(nextLine)
            #  read laser
            if inputCounter == 2:
                laser = nextLine
                laserStartCol = int(laser.substring(0, 1))
                laserStartRow = int(laser.substring(2, 3))
                laserOrientation = str(laser.substring(3))

        in_.close()
        logging.info('closing the input file ' )

        mirrorMaze = [None]*mazeCol
        for m in mirrors:
            if len(m) > 4:
                d = m.substring(3, 4)
                s = m.substring(4)
                tmpMirror = mirror.Mirror(d, s)
            else:
                 d = m.substring(3, 4) 
                 tmpMirror = mirror.Mirror(d)

            col = int(m.substring(0, 1))
            row = int(m.substring(2, 3))     
            mirrorMaze[col][row] = tmpMirror
        mazePath(mirrorMaze, laserStartCol, laserStartRow, laserOrientation)
        logging.info('Maze path', mazePath)
