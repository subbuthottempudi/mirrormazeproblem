import array
import io
import logging
from utils import mirror
from utils import position

        
def mazePath(board, col, row, orientation):
        
        if col < 0 or row < 0 or col >= board.length or row >= board[0].length or (not orientation == "H" and not orientation == "V"):
            print("incorrect input")
            print("maze_patch", col, row, orientation)
            return
        print ("the dimensions of board: " + board.length + " x " + board[0].length)
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

if __name__ == "__main__":
    

        #Logging configuration
        logging.basicConfig(filename='logs/debug.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.disable(logging.DEBUG)
        
        mazeRow = 0
        mazeCol = 0
        mirrors = []
        laserStartRow = -1
        laserStartCol = -1
        laserOrientation = None
        inputCounter = 0

        # in_ = open(args[0],'r')
        contents= open("input/Sample2.txt", 'r')
        logging.info('Opening the input file ')
        
        #  read the configuration for the mirror board and the laser
        #  TO-DO: to catch all kinds of input file exceptions.
        
        print("before while")
        while True:
            line = contents.readline() 
            if not line:break 

            if "-1" in line:
                inputCounter += 1
                continue     
            if line == "\n":
                continue

        #  read maze size
            if inputCounter == 0:
                mazeSize = line.strip()
                print(mazeSize)
                mazeCol = mazeSize.strip().split(",")[0]
                print(mazeCol)
                mazeRow = mazeSize.strip().split(",")[1]
                print(mazeRow)

            #  read mirror
            if inputCounter == 1:

                newline = line.strip()
                mirrors.append(newline)
                print(mirrors)

            #  read laser
            if inputCounter == 2:
                laser = line.strip()
                print(laser)
                laserStartCol = (laser[0:1])
                print("laserStartCol",laserStartCol)
                laserStartRow = laser[2:3]
                print("laserStartRow",laserStartRow)
                laserOrientation = laser[3:4]
                print("laserOrientation",laserOrientation)

        contents.close()
        logging.info('closing the input file ' )

        mirrorMaze =  mirror.onemirror[mazeCol][mazeRow]
        for m in mirrors:
            if len(m) > 4:
              
                d = m[3:4]
                s = m[4:]
                
                tmpMirror = mirror.onemirror(d,s)
            else:
                 d = m[3:4]
                 tmpMirror = mirror.twomirror(d)

            col = m[0:1]
            row = m[2:3]  
            mirrorMaze[col][row] = tmpMirror
        mazePath(mirrorMaze, laserStartCol, laserStartRow, laserOrientation)
        
