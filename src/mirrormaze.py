import sys
import array
import io
import logging
from utils import mirror
from utils import position
        
def mazePath(board, col, row, orientation):
    
    if int(col) < 0 or int(row) < 0 or int(col) >= len(board) or int(row) >= len(board[0]) or (not orientation == "H" and not orientation == "V"):
        print("incorrect input")
        return
    print ("The dimensions of board: " + str(len(board)) + " x " + str(len(board[0])))
    path = []
    direction = "+"
    path.append(position.Position(col, row, orientation, direction))
    print('Extry of laser', path[0])
    last = path[len(path) - 1]
    while (int(last.col) >= 0 and int(last.col) < len(board)) and (int(last.row) >= 0 and int(last.row) < len(board[0])):
        nextPosition(board, path)
        last = path[len(path) - 1]
    print("the path of the laser: ")

    i = 0
    while i < len(path) - 1:
        print(path[i])
        i += 1
    print('Final exit of laser', path[i-1])
        
def nextPosition(board, path):
    """ method nextPosition """
    prev = path[len(path) - 1]
    prevCol = prev.col
    prevRow = prev.row
    prevOrient = prev.orientation
    prevDirection = prev.direction
    nextCol = -1
    nextRow = -1
    nextOrient = prevOrient
    nextDirection = prevDirection

    if prevOrient == "H":
        nextCol = int(prevCol) + (1 if (prevDirection == "+") else - 1)
        nextRow = int(prevRow)

    if prevOrient == "V":
        nextRow = int(prevRow) + (1 if (prevDirection == "+") else - 1)
        nextCol = int(prevCol)

    if (nextCol >= 0 and nextCol < len(board)) and (nextRow >= 0 and nextRow < len(board[0])):
        mirror = board[nextCol][nextRow]
        if mirror != None:
            mirrordir = mirror.strip().split(":")[0]
            mirrorleft = mirror.strip().split(":")[1]
            mirrorright = mirror.strip().split(":")[2]
            if mirrordir == "R":
                if mirrorright == 'True':
                    if prevOrient == "V" and prevDirection == "+":
                        nextOrient = "H"
                        nextDirection = "+"
                    if prevOrient == "H" and prevDirection == "-":
                        nextOrient = "V"
                        nextDirection = "-"
                if mirrorleft == 'True':
                    if prevOrient == "V" and prevDirection == "-":
                        nextOrient = "H"
                        nextDirection = "+"
                    if prevOrient == "H" and prevDirection == "+":
                        nextOrient = "V"
                        nextDirection = "-"
            if mirrordir == "L":
                if mirrorright == 'True':
                    if prevOrient == "V" and prevDirection == "-":
                        nextOrient = "H"
                        nextDirection = "+"
                    if prevOrient == "H" and prevDirection == "-":
                        nextOrient = "V"
                        nextDirection = "+"
                if mirrorleft == 'True':
                    if prevOrient == "V" and prevDirection == "+":
                        nextOrient = "H"
                        nextDirection = "-"
                    if prevOrient == "H" and prevDirection == "+":
                        nextOrient = "V"
                        nextDirection = "-"
    next = position.Position(str(nextCol), str(nextRow), nextOrient, nextDirection)
    for p in path:
        if p == next:
            raise Exception("the laser is trapped in the maze.")
    
    path.append(next)
    

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
    #  TO-DO: catch all kinds of input file exceptions.
    
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
            mazeCol = mazeSize.strip().split(",")[0]
            mazeRow = mazeSize.strip().split(",")[1]

        #  read mirror
        if inputCounter == 1:

            newline = line.strip()
            mirrors.append(newline)

        #  read laser
        if inputCounter == 2:
            laser = line.strip()
            laserStartCol = (laser[0:1])
            laserStartRow = laser[2:3]
            laserOrientation = laser[3:4]

    contents.close()
    logging.info('closing the input file ' )

    mirrorMaze = [[None]*int(mazeCol) for i in range(int(mazeRow))]
    #mirrorMaze = [[]]
    for m in mirrors:
        if len(m) > 4:
            
            d = m[3:4]
            s = m[4:]
            direction, leftSide, rightSide = mirror.onemirror(d,s)
        else:
            d = m[3:4]
            direction, leftSide, rightSide = mirror.twomirror(d)
        col = m[0:1]
        row = m[2:3]  
        mirrorMaze[int(col)][int(row)] = direction + ":" + str(leftSide)+ ":" + str(rightSide)
    mazePath(mirrorMaze, laserStartCol, laserStartRow, laserOrientation)
    
